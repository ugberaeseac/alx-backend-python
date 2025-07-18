import logging
from datetime import datetime


class RequestLoggingMiddleware():
    """
    middleware that logs each user's request
    with timestamp, user and request path
    """
    def __init__(self, get_response):
        """ initialize"""
        self.get_response = get_response
        logging.basicConfig(filename='requests.log', level=logging.INFO)

    def __call__(self, request):
        logging.info(f'{datetime.now()} - User: {request.user} - Path: {request.path}')

        response = self.get_response(request)
        return response

