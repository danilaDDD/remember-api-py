import logging

from django.http import HttpRequest

logger = logging.getLogger('request_logger')

class LoggingNo20xMiddleware:
    """
    Middleware to log requests and responses, excluding 2xx responses.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)

        # Log the response if it's not a 2xx status code
        status = response.status_code
        if status < 200 or status >= 300:
            logger.error(f'Request {request.method.title()}, {request.user}, {request.get_full_path} \nResponse: {status} {response.content.decode()}')

        return response