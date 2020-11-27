from django.db import models

# Create your models here.

class BookingDetail(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    username = models.TextField()

class Payment(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    numticket = models.IntegerField()
    price = models.IntegerField()
    cardnumber = models.IntegerField()