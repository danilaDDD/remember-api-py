from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from account.permissions import PrimaryAccessPermission
from account.serializers import AccountSerializer


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
