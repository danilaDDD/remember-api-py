from rest_framework import serializers

from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    chat_id = serializers.CharField(required=True, allow_blank=False, min_length=5)

    class Meta:
        model = Account
        fields = ['id', 'username', 'password',  'first_name', 'last_name', 'patronymic',
                  'email', 'phone', 'birth_date', 'gender', 'chat_id']
