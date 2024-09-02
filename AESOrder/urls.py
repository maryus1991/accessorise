from django.urls import path
from .views import Wishlist, Set_Order_Cookie, Set_WishList_Cookie

urlpatterns = [
    path('wish-list/', Wishlist, name='Wishlist.order'),
    path('set-order-cookie/<int:pid>/<int:count>', Set_Order_Cookie, name='Order.Set.Cookie'),
    path('set-whishlist-cookie/<int:pid>/<int:count>', Set_WishList_Cookie, name='Wishlist.Set.Cookie')
]