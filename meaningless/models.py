from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthday = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)