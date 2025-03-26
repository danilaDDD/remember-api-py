from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView

from account.views import RegistrationAPIView

app_name = 'account'

urlpatterns = [
    path('', RegistrationAPIView.as_view(), name='registration'),
    path('tokens/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokens/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tokens/verify/', TokenVerifyView.as_view(), name='token_verify'),
]