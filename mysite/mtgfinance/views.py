from django.shortcuts import render, redirect
from .models import Card, UserCollection
import requests
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    card_price = None
    card_image = None
    card_not_found = False
    card_scryfall_id = None
    card_name = request.GET.get('card_name')

    if card_name:
        api_url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"
        response = requests.get(api_url)

        if response.status_code == 200:
            card_data = response.json()
            card_price = card_data['prices']['usd']
            card_image = card_data['image_uris']['normal'] if 'image_uris' in card_data else None
            card_scryfall_id = card_data['id']
        else:
            card_not_found = True

    return render(request, 'homepage.html', {
        'card_price': card_price,
        'card_name': card_name,
        'card_image': card_image,
        'card_scryfall_id': card_scryfall_id,
        'card_not_found': card_not_found
    })

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def add_to_collection(request, scryfall_id):
    card_data = get_card_data_from_scryfall(scryfall_id)
    card_image_url = card_data['image_uris']['normal'] if 'image_uris' in card_data else None

    card, created = Card.objects.get_or_create(
        scryfall_id=scryfall_id,
        defaults={
            'name': card_data['name'], 
            'usd_price': card_data['prices']['usd'], 
            'image_url': card_image_url
        }
    )

    UserCollection.objects.get_or_create(user=request.user, card=card)
    messages.success(request, f'Added {card.name} to your collection!')
    return redirect('dashboard')

def get_card_data_from_scryfall(scryfall_id):
    api_url = f"https://api.scryfall.com/cards/{scryfall_id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    return None

@login_required
def dashboard(request):
    user_cards = UserCollection.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'user_cards': user_cards})
