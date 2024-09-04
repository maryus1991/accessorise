from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from AESProduct.models import Product
from .models import Order, OrderDetail, WishList, WishListDetail


# Create your views here.

@login_required
def Wishlist(request):
    return render(request, 'AESOrder/wishlist.html')


@login_required
def Set_Order(request, pid, count=1, size=None):
    previous_url = request.META.get('HTTP_REFERER')
    response = redirect(previous_url)
    user = request.user
    if user is None:
        return Http404()

    product: Product = Product.active.filter(id=int(pid)).first()
    if product is None:
        return Http404()

    order: Order = Order.active.get_or_create(user=user)[0]
    orderDetail: OrderDetail = order.details.filter(product=product).first()
    if orderDetail is None:
        order.details.create(
            product=product,
            count=int(count),
            size=size,
            FinalPrice=int(product.price) * int(count)
        ).save()
    elif orderDetail is not None:
        orderDetail.count = int(count) + int(orderDetail.count)
        orderDetail.FinalPrice = int(product.price) * int(orderDetail.count)
        if size != 0 and size is not None:
            orderDetail.size = size
        orderDetail.save()
    return response


@login_required
def Set_WishList(request, pid, count):
    previous_url = request.META.get('HTTP_REFERER')
    response = redirect(previous_url)
    user = request.user
    if user is None:
        return Http404()

    product: Product = Product.active.filter(id=int(pid)).first()
    if product is None:
        return Http404()

    wishlist: WishList = WishList.active.get_or_create(user=user)
    if not wishlist[1]:
        wishlist[0].updated = datetime.now()
        wishlist[0].save()

    wishlistDetail = WishListDetail.active.filter(wishlist__id=wishlist[0].id, product=product).first()
    if wishlistDetail is None:
        WishListDetail.active.create(
            wishlist_id=wishlist[0].id,
            product=product
        ).save()

    return response


@login_required
def remove_item_from_wishlist(request, wdid):
    user = request.user
    wish_list: WishListDetail = WishListDetail.active.filter(id=int(wdid)).first()
    wish_list.is_active = False
    wish_list.is_delete = True
    wish_list.save()
    previous_url = request.META.get('HTTP_REFERER')
    response = redirect(previous_url)
    return response


@login_required
def User_basket_details(request):
    user = request.user
    order = Order.active.get_or_create(user=user)[0]
    order_detail = OrderDetail.active.filter(order=order).all()
    context = {
        'order_detail': order_detail,
        'order': order
    }
    return render(request, 'AESOrder/cart.html', context)


@login_required
def User_wishlist_details(request):
    user = request.user
    wishlist = WishList.active.get_or_create(user=user)[0]
    wishlist_detail = WishListDetail.active.filter(wishlist=wishlist).all()
    context = {
        'wishlist_detail': wishlist_detail,
        'wishlist': wishlist
    }
    return render(request, 'AESOrder/wishlist.html', context)
