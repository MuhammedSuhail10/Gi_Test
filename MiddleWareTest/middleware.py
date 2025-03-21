import time
from django.core.cache import cache
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class RateLimitMiddleware(MiddlewareMixin):
    REQUEST_TIME = 300
    REQUEST_LIMIT = 100

    def process_request(self, request):
        ip = self.get_client_ip(request)
        cache_key = f"rate_limit_{ip}"
        request_log = cache.get(cache_key, [])
        current_time = time.time()
        request_log = [timestamp for timestamp in request_log if current_time - timestamp < self.REQUEST_TIME]

        if len(request_log) >= self.REQUEST_LIMIT:
            return JsonResponse(
                {"error": "Rate limit exceeded. Try again later."},
                status=429,
                headers={"X-RateLimit-Remaining": "0"}
            )
        request_log.append(current_time)
        cache.set(cache_key, request_log, timeout=self.REQUEST_TIME)
        remaining_requests = self.REQUEST_LIMIT - len(request_log)
        request.META["X-RateLimit-Remaining"] = str(remaining_requests)

    def process_response(self, request, response):
        remaining_requests = request.META.get("X-RateLimit-Remaining", "unknown")
        response["X-RateLimit-Remaining"] = remaining_requests
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip