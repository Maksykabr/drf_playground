import logging

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Log information about the request and response
        logging.info(f'Request: {request.method} {request.path}')
        logging.info(f'Response: {response.status_code}')
        return response