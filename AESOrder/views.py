from django.shortcuts import render


# Create your views here.
def Wishlist(request):
    return render(request, 'AESOrder/wishlist.html')
