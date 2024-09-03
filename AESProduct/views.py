from django.db.models.aggregates import Count
from django.views.generic import ListView, DetailView
from django.db.models import Q
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
        tag = self.kwargs.get('tag')

        if brand is not None:
            query = Product.active.filter(brands__slug__iexact=brand,
                                          brands__is_active=True,
                                          brands__is_delete=False).all()
        if category is not None:
            query = Product.active.filter(categories__slug__iexact=category,
                                          categories__is_active=True,
                                          categories__is_delete=False).all()

        if tag is not None:
            query = Product.active.filter(tags__slug__iexact=tag,
                                          tags__is_active=True,
                                          tags__is_delete=False).all()
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = (Product_Categories.active.filter(parent=None).prefetch_related('parent').annotate(
            PCount=Count('products')).order_by('-id').all())
        context['brands'] = Product_Brands.active.all()
        return context


class Product_Detail(DetailView):
    model = Product
    template_name = 'AESProduct/variable-products.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product = context['product']
        cid = product.categories.last()
        bid = product.brands.last()
        tid = product.tags.last()

        context['product_related'] = Product.active.filter(
            Q(categories= cid if cid is not None else None) |
            Q(brands= bid if cid is not None else None) |
            Q(tags= tid if cid is not None else None)
        ).exclude(
            id = product.id
        ).order_by(
         '-id',
        ).distinct(
            
        ).all()[:4]

        return context
