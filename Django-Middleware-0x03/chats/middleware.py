import logging
from datetime import datetime
from django.http import HttpResponseForbidden


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


class RestrictAccessByTimeMiddleware():
    """
    middlewate that restricts access to the messaging app
    during certain hours of the day
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour

        if (18 <= current_hour <= 21):
            return HttpResponseForbidden('Access is forbidden outside 6PM and 9PM')
        response = self.get_response(request)
        return response







