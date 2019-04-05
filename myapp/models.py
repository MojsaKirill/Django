from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.title

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notes = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return self.username