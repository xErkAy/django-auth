import jwt
from django.contrib.auth import get_user_model

from rest_framework.exceptions import AuthenticationFailed
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings

from django.utils.translation import gettext_lazy as _

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class CustomJWTAuthentication(JSONWebTokenAuthentication):

    def authenticate(self, request):
        token = self.get_jwt_value(request)

        if token is None:
            return None

        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            msg = _('Signature has expired.')
            raise AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = _('Error decoding signature.')
            raise AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise AuthenticationFailed()
        return self._authenticate_credentials(payload)

    def _authenticate_credentials(self, payload):
        User = get_user_model()
        username = jwt_get_username_from_payload(payload)
        if username:
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                msg = _('Invalid signature.')
                raise AuthenticationFailed(msg)
        else:
            msg = _('Invalid payload.')
            raise AuthenticationFailed(msg)
