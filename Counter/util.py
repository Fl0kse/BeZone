from typing import Dict
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from Counter.models import UserCounter


def check_counter(user: str):
    counter = UserCounter.objects.filter(user=user).first()
    if not counter:
        counter = UserCounter.objects.create(user=user, counter=0)
    return counter


def remove_count(user:str):
    user = User.objects.get(username=user)
    counter = check_counter(user)
    counter.counter -= 1
    counter.save()
    return counter.counter

def add_count(user: str):
    user = User.objects.get(username=user)
    counter = check_counter(user)
    counter.counter += 1
    counter.save()
    return counter.counter


def get_count(user: str):
    user = User.objects.get(username=user)
    counter = check_counter(user)
    return counter.counter


def get_token(user_id: int):
    user = User.objects.get(id=user_id)
    token, created = Token.objects.get_or_create(user=user)
    return token


def check_user_data(user: str, password: str):
    user = User.objects.get(username=user)
    # print(user.password)
    if user.check_password(password):
        return True, user.id
    return False, None


def get_info_login(data: Dict):
    user: str = data['username']
    password: str = data['password']

    return user, password
