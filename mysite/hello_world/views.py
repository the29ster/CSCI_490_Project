from django.shortcuts import render
from .utils import get_card_data
from .models import Card

# Create your views here.

def hello_world(request):
    return render(request, 'hello_world.html', {})

def card_price_view(request, card_name):
    card_data = get_card_data(card_name)
    
    if card_data:
        card, created = Card.objects.get_or_create(
            scryfall_id=card_data['scryfall_id'],
            defaults={
                'name': card_data['name'],
                'usd_price': card_data['usd_price'],
                'eur_price': card_data['eur_price'],
                'tix_price': card_data['tix_price'],
            }
        )
        if not created:
            # Update existing card price
            card.usd_price = card_data['usd_price']
            card.eur_price = card_data['eur_price']
            card.tix_price = card_data['tix_price']
            card.save()
    
        context = {'card': card}
        return render(request, 'card_price.html', context)
    
    return render(request, 'card_not_found.html', {'card_name': card_name})
