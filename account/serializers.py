from rest_framework import serializers

from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    chat_id = serializers.CharField(required=True, allow_blank=False, min_length=5)

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)

    class Meta:
        model = Account
        fields = ['id', 'username', 'password',  'first_name', 'last_name', 'patronymic',
                  'email', 'phone', 'birth_date', 'gender', 'chat_id']

class AccountListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        exclude = ['password', 'is_staff', 'is_superuser', 'is_active', 'last_login',]