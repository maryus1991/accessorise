from django.views.generic import ListView, DetailView

from .models import Product


# Create your views here.
class Product_List(ListView):
    model = Product
    template_name = 'AESProduct/slidebar-left.html'
    context_object_name = 'product'
    paginate_by = 18


class Product_Detail(DetailView):
    model = Product
    template_name = 'AESProduct/variable-products.html'
    context_object_name = 'product'
