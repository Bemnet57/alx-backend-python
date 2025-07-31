# middleware.py
from datetime import datetime
import logging
from datetime import datetime, time
from django.http import HttpResponseForbidden
from django.core.cache import cache
from django.http import JsonResponse
from datetime import datetime


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


# middleware.py

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limit = 5  # 5 messages
        self.time_window = 60  # 60 seconds (1 minute)

    def __call__(self, request):
        # Only apply to POST requests to message API
        if request.method == 'POST' and request.path.startswith('/api/messages'):
            # Get IP address
            ip = self.get_client_ip(request)
            cache_key = f'msg_rate_{ip}'

            # Retrieve current count from cache
            history = cache.get(cache_key, [])
            now = datetime.now().timestamp()

            # Filter timestamps to keep only those in the last 60 seconds
            history = [ts for ts in history if now - ts < self.time_window]

            if len(history) >= self.rate_limit:
                return JsonResponse(
                    {"detail": "Rate limit exceeded. Max 5 messages per minute."},
                    status=429
                )

            # Add current timestamp and update cache
            history.append(now)
            cache.set(cache_key, history, timeout=self.time_window)

        return self.get_response(request)

    def get_client_ip(self, request):
        """Support X-Forwarded-For headers (e.g., behind reverse proxies)"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
