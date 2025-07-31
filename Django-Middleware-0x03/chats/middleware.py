# middleware.py
from datetime import datetime
import logging

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Set up logging
        logging.basicConfig(
            filename='requests.log',
            level=logging.INFO,
            format='%(message)s'
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_message)

        response = self.get_response(request)
        return response

# Task 2
# middleware.py (continue or create if needed)
from datetime import datetime, time
from django.http import HttpResponseForbidden

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define restricted access window (6PM to 9PM)
        now = datetime.now().time()
        start_time = time(18, 0)  # 6:00 PM
        end_time = time(21, 0)    # 9:00 PM

        # Check if request is to the chat API
        is_chat_request = request.path.startswith('/api/conversations') or request.path.startswith('/api/messages')

        if is_chat_request and not (start_time <= now <= end_time):
            return HttpResponseForbidden("Access to the chat system is restricted to 6PM - 9PM only.")

        return self.get_response(request)
