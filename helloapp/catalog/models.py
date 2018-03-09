
from django.db import models



class Person (models.Model):
    id = models.CharField(max_length=20) ,  'primary_key=True'
    brand_manager = models.CharField(max_length=20)
    manager = models.CharField(max_length=20)
    contact_number = models.IntegerField(blank=True, null=True)
    contact_email = models.EmailField(max_length=20)
    country = models.CharField(max_length=20)