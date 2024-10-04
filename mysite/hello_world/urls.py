from django.urls import path
from .views import card_price_view

urlpatterns = [
    path('card/<str:card_name>/', card_price_view, name='card_price'),
]