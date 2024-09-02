from django.db.models.aggregates import Count
from django.views.generic import ListView, DetailView

from .models import Product, Product_Brands, Product_Categories


# Create your views here.
class Product_List(ListView):
    model = Product
    template_name = 'AESProduct/slidebar-left.html'
    context_object_name = 'products'
    paginate_by = 18

    def get_queryset(self):
        query = super().get_queryset()
        brand = self.kwargs.get('brand')
        category = self.kwargs.get('category')

        if brand is not None:
            query = Product.active.filter(product_brands__slug__iexact=brand,
                                          product_brands__is_active=True,
                                          product_brands__is_delete=False).all()
        if category is not None:
            query = Product.active.filter(product_categories__slug__iexact=category,
                                          product_categories__is_active=True,
                                          product_categories__is_delete=False).all()
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = (Product_Categories.active.filter(parent=None).prefetch_related('parent').annotate(PCount=Count('products')).order_by('-id').all())
        context['brands'] = Product_Brands.active.all()

        return context



class Product_Detail(DetailView):
    model = Product
    template_name = 'AESProduct/variable-products.html'
    context_object_name = 'product'
