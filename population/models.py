from django.db import models

# Create your models here.
class Population(models.Model):
    city = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=20, decimal_places=12)
    lng = models.DecimalField(max_digits=20, decimal_places=12)
    country = models.CharField(max_length=200, blank=True)
    iso2 = models.CharField(max_length=5, blank=True)
    admin_name = models.CharField(max_length=100, blank=True)
    capital = models.CharField(max_length=100, blank=True, null=True)
    population = models.DecimalField(max_digits=20, decimal_places=12)
    population_proper= models.DecimalField(max_digits=20, decimal_places=12)
    