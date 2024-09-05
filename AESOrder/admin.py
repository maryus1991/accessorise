from django.contrib import admin
from .models import Order, OrderDetail, WishList, WishListDetail, Coupon

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(WishList)
admin.site.register(WishListDetail)
admin.site.register(Coupon)