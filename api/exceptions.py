from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _


class AuthenticationFailed(APIException):
    default_code = 400
    default_detail = _('Authentication failed')


class InvalidUsernameOrPassword(APIException):
    default_code = 400
    default_detail = _('Invalid username or password')


class ExpiredSignature(APIException):
    default_code = 400
    default_detail = _('Signature has expired')


class DecodeSignature(APIException):
    default_code = 400
    default_detail = _('Error decoding signature')


class InvalidSignature(APIException):
    default_code = 400
    default_detail = _('Invalid signature')


class InvalidPayload(APIException):
    default_code = 400
    default_detail = _('Invalid payload')


class JWTTokenNotFound(APIException):
    default_code = 400
    default_detail = _('Authorization token has not been found')
