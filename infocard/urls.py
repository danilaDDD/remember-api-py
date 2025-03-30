from django.urls import path

from infocard.views import RememberListAPIView

app_name = 'infocard'

urlpatterns = [
    path('waited-remembers/', RememberListAPIView.as_view(), name='remembers'),
]