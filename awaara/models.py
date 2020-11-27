from django.db import models

# Create your models here.

class Destination(models.Model):
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    offer = models.BooleanField(default=False)

class Reviews(models.Model):
    img = models.ImageField(upload_to='pics')
    review = models.TextField()