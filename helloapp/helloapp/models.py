from django.db import models

class Artist(models.Model):
    id = models.IntegerField(max_length=20), 'primary_key=True'
    BandName = models.CharField(max_length=20)
    Manager = models.CharField(max_length=20)
    ContactNumber = models.CharField(max_length=12)
    ContactEmail = models.EmailField(max_length=20)
    Country = models.CharField(max_length=20)