from django.db import models

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

