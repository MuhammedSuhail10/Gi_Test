from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name