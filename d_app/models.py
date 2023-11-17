from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.IntegerField()

# class YourModel(models.Model):
#     image = models.ImageField(upload_to='photos/')
