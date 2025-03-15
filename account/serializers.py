from datetime import datetime

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenObtainPairSerializer, \
    TokenRefreshSerializer

from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    chat_id = serializers.CharField(required=True, allow_blank=False, min_length=5)

    class Meta:
        model = Account
        fields = ['id', 'username', 'password',  'first_name', 'last_name', 'patronymic',
                  'email', 'phone', 'birth_date', 'gender', 'chat_id']


class CustomObtainTokenSerializer(TokenObtainPairSerializer):
    expiration_date: datetime = None

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        cls.expiration_date = datetime.fromtimestamp(token['exp'])

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data['expirationSeconds'] = int((self.expiration_date - datetime.now()).total_seconds())

        return data