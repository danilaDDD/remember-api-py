from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from common.views import BaseAuthenticateAPIView
from infocard.serializers import RememberSerializer
from infocard.handlers import RememberHandler


class RememberListAPIView(BaseAuthenticateAPIView):
    serializer_class = RememberSerializer
    http_method_names = ['get', ]
    remember_handler = RememberHandler()

    @swagger_auto_schema(
        tags=['remembers'],
        operation_summary='Получения списка повторений',
    )
    def get(self, request: Request) -> Response:
        try:
            remembers = self.remember_handler.list(request)
            serializer = self.serializer_class(remembers, many=True)
        except ValidationError as e:
            return Response({'error': str(e)}, status=400)

        return Response(serializer.data)



