from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class BaseAuthenticateAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]