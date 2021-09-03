import json

from django.http import HttpResponse
from rest_framework.views import APIView

from .exception import UnauthorizedException
from Counter.util import get_token, check_user_data, get_info_login


class CounterView(APIView):

    def _check_auth(self, request, *args, **kwargs):
        is_authenticated: bool = request.user is not None and request.user.is_authenticated
        if not is_authenticated:
            raise UnauthorizedException()

    def get(self, request):
        self._check_auth(request)


class LoginView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        user, password = get_info_login(data)

        res, user_id = check_user_data(user, password)

        if res:
            response = HttpResponse()
            token = get_token(user_id=user_id)
            response.set_cookie(key='token', value=token, secure=True)
            response.cookies["token"]['SameSite'] = "None"
            response['token'] = token
            return response
        return HttpResponse("User is not found")
