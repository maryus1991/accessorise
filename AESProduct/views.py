from django.db.models.aggregates import Count
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Product, Product_Brands, Product_Categories, Product_comment


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


        find = self.request.GET.get('search')

        if find is not None:
            query = Product.active.filter(
                Q(description__contains=find) | Q(title__contains=find)|
                Q(short_description__contains=find) | Q(more_details__contains=find)|
                Q(slug__contains=find)
            ).all()
            return query

        if brand is not None:
            query = Product.active.filter(brands__slug__iexact=brand,
                                          brands__is_active=True,
                                          brands__is_delete=False).all()
            return query
        if category is not None:
            query = Product.active.filter(categories__slug__iexact=category,
                                          categories__is_active=True,
                                          categories__is_delete=False).all()
            return query

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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(**kwargs)
        cid = request.POST.get('cid')
        try:
            if cid !=  '':
                cid = Product_comment.objects.filter(id=cid).first()
                cid.is_delete = True
                cid.save()
                return self.render_to_response(context)
        except:
            cid = ''
        Message = request.POST.get('Message')
        email = request.POST.get('email')
        name = request.POST.get('name')
        pid = request.POST.get('pid')
        star_rate = request.POST.get('star_rate')
        comment_parent = request.POST.get('comment_parent')
        product = self.get_object()
        if star_rate == '':
            star_rate = None

        if Message == '' or name == '' or pid == '' or email == '' or product.id != int(pid) :
            context['err'] = 'لطفا اطلاعات را کامل وارد کنید و سپس نظرات را ارسال کنید'

            return self.render_to_response(context)

        try:
            comment_parent = Product_comment.active.filter(id=comment_parent).first()
        except:
            comment_parent = None

        Product_comment.active.create(
            full_name=name,
            email=email,
            comment=Message,
            rate=star_rate,
            product=product,
            parent =  comment_parent,
        ).save()
        return  self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product = context['product']
        context['comments'] = Product_comment.active.filter(
            parent=None, product=product
            ).all()
        context['comments_count'] = Product_comment.active.filter(
            product=product
            ).count()
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
