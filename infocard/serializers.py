from rest_framework import serializers

from infocard.models import Remember


class RememberSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='get_question', required=True)
    answer = serializers.CharField(source='get_answer', required=True)
    tags_text = serializers.CharField(source='info_card.tags_text', read_only=True)

    class Meta:
        model = Remember
        fields = [
            'id',
            'tags_text',
            'question',
            'answer',
            'real_answer',
            'date',
            'status',
        ]