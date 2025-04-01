from django.urls import path
import trainings.views as views

app_name = 'trainings'

urlpatterns = [
    path('trainings/', views.CreateTrainingAPIView.as_view(), name='create_training'),
]