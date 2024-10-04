from django.urls import path
from hello_world import views
from .views import card_price_view

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('card/<str:card_name>/', card_price_view, name='card_price'),
]