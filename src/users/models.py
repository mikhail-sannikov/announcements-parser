from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    patronymic = models.CharField('отчество', max_length=255, blank=True)

    REQUIRED_FIELDS = []

    @property
    def fullname(self) -> str:
        return ' '.join(filter(bool, (self.last_name, self.first_name, self.patronymic)))
