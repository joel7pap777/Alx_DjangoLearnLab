from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following",
        blank=True,
    )