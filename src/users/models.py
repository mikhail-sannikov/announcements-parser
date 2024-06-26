from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    patronymic = models.CharField('отчество', max_length=255, blank=True)

    REQUIRED_FIELDS = []
