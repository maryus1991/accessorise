from django.urls import path
from .views import  (Set_Order,
                     Set_WishList,User_basket_details
                    ,User_wishlist_details,
                     remove_item_from_wishlist,
                     remove_item_from_basket,
                     change_details_count,
                     coupon,
                     complete_order
                     )

urlpatterns = [
    path('set-order-cookie/<int:pid>/<int:count>', Set_Order, name='Order.Set.Cookie'),
    path('set-order-cookie-size/<int:pid>/<int:count>/<str:size>/', Set_Order, name='Order.size.Set.Cookie'),
    path('set-whishlist-cookie/<int:pid>/<int:count>', Set_WishList, name='Wishlist.Set.Cookie'),
    path('User-basket-details/', User_basket_details, name='User.basket.details'),
    path('User-wishlist-details/', User_wishlist_details, name='User.wishlist.details'),
    path('User-wishlist-details/', User_wishlist_details, name='Wishlist.order'),
    path('User-wishlist-details-remove/<int:wdid>', remove_item_from_wishlist, name='User.remove.wishlist.details'),
    path('User-basket-details-remove/', remove_item_from_basket, name='User.remove.basket.details'),
    path('User-basket-details-count/', change_details_count, name='User.change.count.basket.details'),
    path('User-basket-details-coupon/', coupon, name='User.coupon.basket.details'),
    path('User-complete-order/', complete_order, name='User.complete.order'),
]