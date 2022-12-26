from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    status = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255, default='-')
    avatar = models.ImageField(upload_to='avatars', default='default.png', blank=True)
    birth_date = models.DateField(null=True, blank=True)


class UserSettings(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE)
