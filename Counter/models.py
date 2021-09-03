from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User


# Create your models here.
class UserCounter(Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    counter = models.IntegerField(default=0, verbose_name='Счетчик')