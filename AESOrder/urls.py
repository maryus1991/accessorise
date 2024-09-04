from django.urls import path
from .views import Wishlist, Set_Order, Set_WishList,User_basket_details ,User_wishlist_details, remove_item_from_wishlist

urlpatterns = [
    path('wish-list/', Wishlist, name='Wishlist.order'),
    path('set-order-cookie/<int:pid>/<int:count>', Set_Order, name='Order.Set.Cookie'),
    path('set-order-cookie-size/<int:pid>/<int:count>/<str:size>/', Set_Order, name='Order.size.Set.Cookie'),
    path('set-whishlist-cookie/<int:pid>/<int:count>', Set_WishList, name='Wishlist.Set.Cookie'),
    path('User-basket-details/', User_basket_details, name='User.basket.details'),
    path('User-wishlist-details/', User_wishlist_details, name='User.wishlist.details'),
    path('User-wishlist-details-remove/<int:wdid>', remove_item_from_wishlist, name='User.remove.wishlist.details')
]