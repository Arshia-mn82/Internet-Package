from django.db import models
from provider.models import Provider

class InternetPackage(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    providers = models.ForeignKey(Provider,on_delete=models.CASCADE)
