from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=400)
    user_id = models.FloatField()

    def __str__(self):
        return self.title