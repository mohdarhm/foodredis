from django.db import models
from django.contrib.auth.models import User

class SourceInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    region = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=15)
    email = models.EmailField()

class DistributorInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    phoneno = models.CharField(max_length=15)
    email = models.EmailField()

class Listings(models.Model):
    source = models.OneToOneField(SourceInfo, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    FOOD_TYPES = [
        ('prepared', 'Prepared Food'),
        ('groceries', 'Groceries'),
    ]
    food_type = models.CharField(max_length=20, choices=FOOD_TYPES)
