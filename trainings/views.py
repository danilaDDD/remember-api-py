from rest_framework.request import Request
from rest_framework.serializers import ValidationError
from rest_framework.response import Response

from common.utils import get_or_404
from common.views import BaseAuthenticateAPIView
from trainings.models import RememberItem, Training
from trainings.serializers import CreateTrainingSerializer, TrainingSerializer, TrainingItemSerializer, \
    TrainingItemUpdateSerializer


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


class TrainingItemsAPIView(BaseAuthenticateAPIView):
    serializer_class = TrainingItemSerializer
    http_method_names = ['get']

    def get(self, request: Request, training_id: int, **kwargs):
        training = get_or_404(Training, id=training_id,)
        if request.query_params.get('index') is not None:
            remember_items = (training.items
                              .filter(index=int(request.query_params['index']), is_active=True))
        else:
            remember_items = training.items.filter(is_active=True)

        serializer = TrainingItemSerializer(remember_items, many=True)
        return Response(serializer.data)


class PutTrainingItemAPIView(BaseAuthenticateAPIView):
    serializer_class = TrainingItemUpdateSerializer
    http_method_names = ['put']

    def put(self, request: Request, training_id: int, item_id: int, **kwargs):
        remember_item = get_or_404(RememberItem, id=item_id, is_active=True)
        serializer = self.get_serializer(data=request.data, instance=remember_item)
        if serializer.is_valid():
            remember_item = serializer.save()
            resp_serializer = TrainingItemSerializer(instance=remember_item)
            return Response(resp_serializer.data)

        else:
            return Response(serializer.errors, status=400)

