from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from account.views import RegistrationAPIView

app_name = 'account'

urlpatterns = [
    path('', RegistrationAPIView.as_view(), name='registration'),
    path('tokens/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]