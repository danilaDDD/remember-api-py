from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from account.models import Account
from account.permissions import PrimaryAccessPermission
from account.serializers import AccountSerializer, AccountListSerializer


# Create your views here.
class RegistrationAPIView(GenericAPIView):
    serializer_class = AccountSerializer
    permission_classes = [PrimaryAccessPermission]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAccountsAPIView(GenericAPIView):
    serializer_class = AccountListSerializer
    permission_classes = [PrimaryAccessPermission]
    http_method_names = ['get']

    def get(self, request: Request):
        accounts = Account.objects.filter(is_active=True, is_staff=False)

        chat_id: int | None= request.query_params.get('chat-id')
        if chat_id is not None:
            accounts = accounts.filter(chat_id=chat_id)

        serializer = self.serializer_class(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)