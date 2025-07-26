from django.db import models

# Create your models here.
class student(models.Model):
    studName = models.TextField(max_length=10)
    age = models.IntegerField(max_length=2)
    stream = models.TextField(max_length=10)
    marks = models.IntegerField(max_length=3)
    city = models.TextField(max_length=15)