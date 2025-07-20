import logging
from datetime import datetime, timedelta
from django.http import HttpResponseForbidden, JsonResponse


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


class OffensiveLanguageMiddleware():
    """
    middleware that limits the number of chat messages a user
    can send within 1 minute
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.timestamp_log = {}
        self.limit = 5

    def __call__(self, request):
        if request.method == 'POST' and request.path.startswith('/api/conversations/'):
            ip = self.get_ip(request)
            time_now = datetime.now()

            if ip not in self.timestamp_log:
                self.timestamp_log[ip] = []

            time = time_now - timedelta(minutes=1)
            timestamp_list = []
            for timestamp in self.timestamp_log[ip]:
                if timestamp > time:
                    timestamp_list.append(timestamp)
            self.timestamp_log[ip] = timestamp_list

            if len(self.timestamp_log[ip]) >= self.limit:
                return JsonResponse({'error': 'Rate limit exceeded'}, status=429)

            self.timestamp_log[ip].append(time_now)


        response = self.get_response(request)
        return response


    def get_ip(self, request):
        """ get ip address of the request"""
        ip = request.META.get('REMOTE_ADDR')
        if ip:
            return ip


class RolepermissionMiddleware():
    """
    middleware that checks if admin/moderator
    before allowing access to certain routes
    """

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        protected_routes = ['/admin/',]

        if request.path in protected_routes:
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Authorization required'}, status=401)

            if not (request.user.is_superuser or request.user.is_staff):
                return JsonResponse({'error': 'Permission denied'}, status=403)

        response = self.get_response(request)
        return response

