from django.shortcuts import render, redirect


# Create your views here.
def Wishlist(request):
    return render(request, 'AESOrder/wishlist.html')


def Set_Order_Cookie(request, pid, count=1, size=None):
    previous_url = request.META.get('HTTP_REFERER')
    response = redirect(previous_url)
    print(pid,count,size)
    return response


def Set_WishList_Cookie(request, pid, count):
    previous_url = request.META.get('HTTP_REFERER')
    response = redirect(previous_url)
    return response
