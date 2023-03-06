from django.db import models
from django.utils import timezone

class Species(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

class Animal(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    last_feed_time = models.DateTimeField(auto_now=True)


# Create your models here.
