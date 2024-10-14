from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=200)
    scryfall_id = models.CharField(max_length=100, unique=True)
    usd_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return self.name

class UserCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.card.name}'