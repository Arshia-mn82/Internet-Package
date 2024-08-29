from django.db import models
from package.models import InternetPackage

class Provider(models.Model):
    name = models.CharField(max_length=50)
    verification = models.BooleanField(default=False)
    


