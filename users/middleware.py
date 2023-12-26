from django.contrib.auth import middleware
from django.urls import reverse
from django.utils.functional import SimpleLazyObject

from .authentication import CognitoAuthenticationMixin
from .exceptions import NoAuthToken


class CognitoAuthMiddleware(
    CognitoAuthenticationMixin, middleware.AuthenticationMiddleware
):
    @staticmethod
    def get_auth_token(request):
        try:
            return request.META["HTTP_AUTHORIZATION"]
        except Exception:
            raise NoAuthToken()

    def process_request(self, request):
        if request.path.startswith(reverse("admin:index")):
            return None
        request.user = SimpleLazyObject(lambda: self.authenticate(request))