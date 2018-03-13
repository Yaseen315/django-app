from django.db import models

class ARTISTS(models.Model):
    id = models.IntegerField(max_length=20), 'primary_key=True'
    BandName = models.CharField(max_length=20)
    Manager = models.CharField(max_length=20)
    ContactNumber = models.CharField(max_length=12)
    ContactEmail = models.EmailField(max_length=20)
    Country = models.CharField(max_length=20)

class Customers(models.Model):
    id = models.IntegerField(max_length=20), 'primary_key=True'
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Title = models.CharField(max_length=5)
    PhoneNumber = models.CharField(max_length=20)
    StreetAddress = models.CharField(max_length=50)
    PostalCode = models.CharField(max_length=50)
    State = models.CharField(max_length=20)
    Country = models.CharField(max_length=20)
    CountryCode = models.CharField(max_length=20)
    TicketsBought = models.CharField(max_length=20)