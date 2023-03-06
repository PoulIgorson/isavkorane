from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    #username = models.CharField(max_length=255, default='-')
    status = models.CharField(max_length=255, default="status")


class UserSettings(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE)


class Page(models.Model):
    name = models.CharField(max_length=255, unique=True)
    header = models.CharField(max_length=255)
    url = models.CharField(max_length=255)


class TypeBlock(models.Choices):
    TEXT = "Текст"
    IMAGE = "Изображение"


class Block(models.Model):
    type = models.CharField(max_length=255, choices=TypeBlock.choices, default=TypeBlock.TEXT)
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to="pages", blank=True)
