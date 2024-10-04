from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=200)
    scryfall_id = models.CharField(max_length=100, unique=True)
    usd_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    eur_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tix_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.name
