from rest_framework import serializers

from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password',  'first_name', 'last_name', 'patronymic',
                  'email', 'phone', 'birth_date', 'gender']
