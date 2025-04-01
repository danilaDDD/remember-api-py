from rest_framework.serializers import ValidationError
from rest_framework.response import Response

from common.views import BaseAuthenticateAPIView
from trainings.models import RememberItem
from trainings.serializers import CreateTrainingSerializer, TrainingSerializer


# Create your views here.
class CreateTrainingAPIView(BaseAuthenticateAPIView):
    serializer_class = CreateTrainingSerializer
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            training = serializer.create_training(account_id=request.user.id)

        except ValidationError as e:
            return Response({'error': e.detail}, status=400)
        except RememberItem.DoesNotExist as e:
            return Response({'error': str(e)}, status=400)

        serializer = TrainingSerializer(instance=training)

        return Response(serializer.data)

