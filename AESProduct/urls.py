from django.urls import path

from . import views

urlpatterns = [
    path('', views.Product_List.as_view(), name='product.list.product'),
    path('<pk>', views.Product_Detail.as_view(), name='product.details.product')]
