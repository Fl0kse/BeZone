from rest_framework.exceptions import APIException


class UnauthorizedException(APIException):
    status_code = 401
    default_detail = 'result: unauthorized'
    default_code = 'unauthorized'
