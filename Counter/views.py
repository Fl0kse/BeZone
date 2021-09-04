import json
from django.contrib import auth
from django.http import HttpResponse
from rest_framework.views import APIView

from .exception import UnauthorizedException
from Counter.util import get_info_login, get_count, add_count, remove_count


class CounterView(APIView):

    def _check_auth(self, request, *args, **kwargs):
        is_authenticated: bool = request.user is not None and request.user.is_authenticated
        if not is_authenticated:
            raise UnauthorizedException()

    def get(self, request):
        self._check_auth(request)
        return HttpResponse(get_count(request.user.username))

    # Need to set X-CSRFToken in headers
    def post(self, request):
        self._check_auth(request)
        return HttpResponse(add_count(request.user.username))

    def delete(self, request):
        self._check_auth(request)
        return HttpResponse(remove_count(request.user.username))


class CustomAuthToken(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        username, password = get_info_login(data)
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponse("Authorized")
        else:
            return HttpResponse("Unauthorized")
