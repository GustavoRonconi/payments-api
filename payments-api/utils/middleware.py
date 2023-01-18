from django.conf import settings
from log_request_id import REQUEST_ID_HEADER_SETTING
from log_request_id.middleware import RequestIDMiddleware


class FallbackRequestIDMiddleware(RequestIDMiddleware):
    def _get_request_id(self, request):
        request_id = None

        request_id_header = getattr(settings, REQUEST_ID_HEADER_SETTING, None)
        if request_id_header:
            request_id = request.META.get(request_id_header)

        if not request_id:
            request_id = self._generate_id()

        return request_id
