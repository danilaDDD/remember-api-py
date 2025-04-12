import logging

import pytz
from django.http import HttpRequest
from django.utils import timezone

logger = logging.getLogger('request_logger')

class CustomCommonMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        timezone.activate(pytz.timezone('Europe/Moscow'))
        response = self.get_response(request)

        # Log the response if it's not a 2xx status code
        status = response.status_code
        if status < 200 or status >= 300:
            logger.error(f'Request {request.method.title()}, {request.user}, {request.get_full_path} \nResponse: {status} {response.content.decode()}')

        return response