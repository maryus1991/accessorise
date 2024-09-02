from django.urls import path

from . import views

urlpatterns = [
    path('', views.Product_List.as_view(), name='product.list.product'),
    path('<pk>', views.Product_Detail.as_view(), name='product.details.product'),
    path('brands/<slug:brand>', views.Product_List.as_view(), name='brands.product.list.product'),
    path('categories/<slug:category>', views.Product_List.as_view(), name='categories.product.list.product'),
    path('sort/<str:sort>', views.Product_List.as_view(), name='sort.product.list.product')
]
