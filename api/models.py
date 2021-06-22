from django.db import models

# Create your models here.
class Roadtrip (models.Model):
    name = models.CharField(max_length=30)
    numberOfPassengers = models.IntegerField()