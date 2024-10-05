from django.shortcuts import render, redirect
from .utils import get_card_data
from .models import Card
import requests
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def homepage(request):
    card_price = None
    card_image = None
    card_not_found = False
    card_name = request.GET.get('card_name')

    if card_name:
        # Scryfall API search for the card name
        api_url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"
        response = requests.get(api_url)

        if response.status_code == 200:
            card_data = response.json()
            card_price = card_data['prices']['usd']  # Fetch USD price
            card_image = card_data['image_uris']['normal'] if 'image_uris' in card_data else None
        else:
            card_not_found = True

    return render(request, 'homepage.html', {
        'card_price': card_price,
        'card_name': card_name,
        'card_image': card_image,
        'card_not_found': card_not_found
    })

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})