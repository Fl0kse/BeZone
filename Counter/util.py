from typing import Dict
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


def get_token(user_id: int):
    user = User.objects.get(id=user_id)
    token, created = Token.objects.get_or_create(user=user)
    return token


def check_user_data(user: str, password: str):
    user = User.objects.filter(username=user).first()
    # print(user.password)
    if user.check_password(password):
        return True, user.id
    return False, None


def get_info_login(data: Dict):
    user: str = data['user']
    password: str = data['password']

    return user, password
