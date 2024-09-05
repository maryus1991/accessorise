from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.shortcuts import reverse

from AESProduct.models import Product
from .models import Order, OrderDetail, WishList, WishListDetail


# Create your views here.

@login_required
def change_details_count(request):
    if request.method == 'POST':
        count = int(request.POST.get('count'))
        did = int(request.POST.get('did'))
        if count > 0 and did > 0:
            orderDetail: OrderDetail = OrderDetail.active.filter(id=did).first()
            product = orderDetail.product
            if orderDetail is not None:
                product_stock = orderDetail.product.stock
                if product_stock >= count:
                    if product.has_size:
                        size = product.products_sizes_set.filter(size=orderDetail.size).first()
                        if size.count > count:
                            count = count
                        else:
                            count = size.count
                    orderDetail.count = count
                    orderDetail.save()

    final_price: Order = Order.active.filter(user=request.user).first()
    final_price.total_price = final_price.get_final_price()
    final_price.save()
    return redirect(reverse('User.basket.details'))


@login_required
def Set_Order(request, pid, count=1, size=None):
    size_url = size
    previous_url = request.META.get('HTTP_REFERER')
    response = redirect(previous_url)
    user = request.user
    if user is None:
        return Http404()

    product: Product = Product.active.filter(id=int(pid)).first()
    if product is None:
        return Http404()

    if count > product.stock or count < 0:
        return response

    order: Order = Order.active.get_or_create(user=user)[0]
    orderDetail: OrderDetail = order.details.filter(product=product).first()
    if count < 0 or product.stock < 0:
        return Http404()
    if orderDetail is None:
        if product.off is not None or int(product.off if product.off is not None else 0) > 0:
            FinalPrice = int(product.price * (1 - int(product.off) / 100)) * int(count)
        else:
            FinalPrice = int(product.price) * int(count)

        if size_url is not None and product.has_size:
            size = product.products_sizes_set.filter(size=size_url).first()

            if size.count >= count:
                size = size.size
            else:
                count = size.count
                size = size.size
        else:
            size = None

        order.details.create(
            product=product,
            count=int(count),
            size=size,
            FinalPrice=FinalPrice,
        ).save()

    elif orderDetail is not None:
        if product.stock >= int(count) + int(orderDetail.count):
            orderDetail.count = int(count) + int(orderDetail.count)
        elif product.stock < int(count) + int(orderDetail.count):
            orderDetail.count = product.stock

        if size_url is not None and product.has_size:
            size = product.products_sizes_set.filter(size=size_url).first()
            if size.count >= count:
                size = size.size
            else:
                count = size.count
                size = size.size
        else:
            size = None

        if product.off is not None or int(product.off if product.off is not None else 0) > 0:
            FinalPrice = int(product.price * (1 - int(product.off) / 100)) * int(count)
        else:
            FinalPrice = int(product.price) * int(count)

        orderDetail.count = count
        orderDetail.FinalPrice = FinalPrice
        orderDetail.size = size
        orderDetail.save()

    final_price: Order = Order.active.filter(user=request.user).first()
    final_price.total_price = final_price.get_final_price()
    final_price.save()

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
    order_detail = OrderDetail.active.filter(order=order).prefetch_related('product').all()
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


@login_required
def remove_item_from_basket(request):
    if request.method == 'POST':
        user = request.user
        did = request.POST.get('did')
        if did is not None:
            order_detail = OrderDetail.active.filter(id=int(did)).first()
            if order_detail is None:
                return Http404()
            order_detail.is_active = False
            order_detail.save()

            final_price: Order = Order.active.filter(user=request.user).first()
            final_price.total_price = final_price.get_final_price()
            final_price.save()

            previous_url = request.META.get('HTTP_REFERER')
            response = redirect(previous_url)
            return response
        else:
            final_price: Order = Order.active.filter(user=request.user).first()
            final_price.total_price = final_price.get_final_price()
            final_price.save()

            previous_url = request.META.get('HTTP_REFERER')
            response = redirect(previous_url)
            return response


@login_required
def complete_order(request):
    user = request.user
    if user.addr is None or user.post is None:
        return redirect(reverse('Dashboard.account') + '?code=121&status=لطفا ادرس و کد پستی خود را ثبت کنید')
    order: Order = Order.active.filter(user=user).first()
    if order is not None:
        for detail in order.details.all():
            count = detail.count
            if count <= detail.product.stock:

                if detail.product.has_size:
                    if detail.size is None:
                        return redirect(reverse('product.details.product', kwargs={'pk':detail.product.id}) +
                                        '?status=لطفا سایز را انتخاب کنید&code=121')
                    size = detail.product.products_sizes_set.filter(size=detail.size).first()
                    if size.count <= 0:
                        return redirect(reverse('product.details.product', kwargs={'pk':detail.product.id}) +
                                        '?status=سایز مورد نظر تموم شده است&code=121')
                    if size.count >= count:
                        size.count -= count
                        size.save()

                detail.product.stock -= int(count)
                detail.product.save()

        order.total_price = int(order.total_price) + int(order.send_price)
        order.is_paid = True
        order.save()
        return redirect(reverse('User.complete.thsnaks.order'))
    else:
        return redirect(reverse('product.list.product'))


@login_required
def thanks_for_shopping(request):
    return render(request, 'AESOrder/thank-you.html')


def coupon(request):
    # if request.method == 'POST':
    #     coupon_code = request.POST.get('coupon_code')
    #     if coupon_code is not None:
    #         coupon = Coupon.active.filter(slug=coupon_code).first()
    #         if coupon.off_percent is not None:
    #             pass

    return redirect(reverse('User.basket.details'))
