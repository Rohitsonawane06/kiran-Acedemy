from django.db import models

class Bookinfo(models.Model):

    book_name=models.CharField(max_length=20)
    author=models.CharField(max_length=10)
    price=models.FloatField()
    stock=models.IntegerField()
    category=models.CharField(max_length=15)