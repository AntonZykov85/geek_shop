from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    image = models.ImageField(upload_to='users_image',blank=True)
    age = models.PositiveIntegerField(default=18)