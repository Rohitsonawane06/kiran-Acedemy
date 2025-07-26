from django.db import models

# Create your models here.
class student(models.Model):
    roll=models.IntegerField(max_length=2)
    studname=models.TextField(max_length=8)
    studage=models.FloatField()
    stream=models.TextField(max_length=10)
    marks=models.IntegerField()


    def __str__(self):
        return self.studname
