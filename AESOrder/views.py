from django.shortcuts import render

from AESUtils.set_cookies import request_set_cookies_and_render


# Create your views here.
def Wishlist(request):
    return render(request, 'AESOrder/wishlist.html')


def Set_Order_Cookie(request, pid, count=1):
    return request_set_cookies_and_render(request, f'OL_{request.user.username}',
                                          f'{pid}.{count};')


def Set_WishList_Cookie(request, pid, count=1):
    return request_set_cookies_and_render(request, f'WL_{request.user.username}',
                                          f'{pid}.{count};')
