from django.db import models
from package.models import InternetPackage

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    wallet = models.FloatField(default=100000)
    buyed_packages = models.ManyToManyField(InternetPackage)
    
    

