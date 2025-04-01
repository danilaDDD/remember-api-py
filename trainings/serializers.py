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
    day = serializers.DateField(source='get_day')
    question = serializers.CharField(source='remember.get_question')
    answer = serializers.CharField(source='remember.get_answer')
    real_answer = serializers.CharField(source='remember.real_answer')

    class Meta:
        model = RememberItem
        fields = [
            'id',
            'day',
            'question',
            'answer',
            'real_answer',
            'index',
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


