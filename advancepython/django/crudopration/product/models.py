from django.db import models

# Create your models here.
class product(models.Model):
    pname=models.TextField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=330)
    offer=models.TextField(max_length=300)
    productimages=models.ImageField(upload_to='profile_pics/',null=True,blank=True)
    category=models.TextField(max_length=20)


    def __str__(self):
        return self.pname