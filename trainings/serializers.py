import datetime

from rest_framework import serializers

from infocard.models import Remember
from trainings.models import Training, RememberItem


class CreateTrainingSerializer(serializers.Serializer):
    limit = serializers.IntegerField(required=True, max_value=50)

    def create_training(self, account_id: int) -> Training:
        limit = self.validated_data['limit']
        now_day = datetime.datetime.now().date()
        remembers = (Remember.objects
                     .waited_answer(account_id=account_id, day=now_day, limit=limit)
                     .order_by('-day'))
        remember_count = remembers.count()
        if remember_count == 0:
            raise RememberItem.DoesNotExist('Нет карточек для тренировки')

        training = Training(limit=limit, account_id=account_id, remember_count=remembers.count())
        training.save()

        items = []
        for index, remember in enumerate(remembers):
            items.append(RememberItem(training=training, remember=remember, index=index))

        RememberItem.objects.bulk_create(items)
        return training


class TrainingItemSerializer(serializers.ModelSerializer):
    day = serializers.DateField(source='remember.day')
    question = serializers.CharField(source='remember.get_question')
    answer = serializers.CharField(source='remember.get_answer')
    real_answer = serializers.CharField(source='remember.real_answer')
    status = serializers.CharField(source='remember.status')

    class Meta:
        model = RememberItem
        fields = [
            'id',
            'day',
            'status',
            'question',
            'answer',
            'real_answer',
            'index',
        ]

class TrainingItemUpdateSerializer(serializers.ModelSerializer):
    real_answer = serializers.CharField(source='remember.real_answer')
    status = serializers.ChoiceField(choices=Remember.STATUSES)

    def update(self, instance: RememberItem, validated_data: dict) -> RememberItem:
        remember = instance.remember
        remember.real_answer = validated_data['remember']['real_answer']
        remember.status = validated_data['status']
        remember.save()

        return instance

    class Meta:
        model = RememberItem
        fields = [
            'id',
            'real_answer',
            'status',
        ]


class TrainingSerializer(serializers.ModelSerializer):
    items = TrainingItemSerializer(many=True)

    class Meta:
        model = Training
        fields = [
            'id',
            'remember_count',
            'limit',
            'items'
        ]


