from django.urls import path
from .views import Wishlist

urlpatterns = [
    path('wish-list/', Wishlist, name='Wishlist.order')
]