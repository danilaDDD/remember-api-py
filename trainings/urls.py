from django.urls import path
import trainings.views as views

app_name = 'trainings'

urlpatterns = [
    path('trainings/', views.CreateTrainingAPIView.as_view(), name='create_training'),
    path('trainings/<int:training_id>/items', views.TrainingItemsAPIView.as_view(), name='training_items'),
    path('trainings/<int:training_id>/items/<int:item_id>/', views.PutTrainingItemAPIView.as_view(), name='update_training_item'),
]