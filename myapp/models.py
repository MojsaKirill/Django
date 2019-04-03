from django.db import models

# Create your models here.
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.title

