import jwt
from django.contrib.auth import get_user_model

from authentication.exceptions import (
    AuthenticationFailed,
    ExpiredSignature,
    InvalidSignature,
    InvalidPayload,
    DecodeSignature,
    JWTTokenNotFound
)
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class CustomJWTAuthentication(JSONWebTokenAuthentication):

    def authenticate(self, request):
        token = self.get_jwt_value(request)

        if token is None:
            raise JWTTokenNotFound()

        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            raise ExpiredSignature()
        except jwt.DecodeError:
            raise DecodeSignature()
        except jwt.InvalidTokenError:
            raise AuthenticationFailed()
        
        user = self._authenticate_credentials(payload)
        return (user, token)

    def _authenticate_credentials(self, payload):
        User = get_user_model()
        username = jwt_get_username_from_payload(payload)
        if username:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise InvalidSignature()
        else:
            raise InvalidPayload()
        
        return user
