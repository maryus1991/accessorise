from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index.home'),
    path('contact-us', views.Contact_Us.as_view(), name='contact-us.home'),
    path('about-us', views.AboutUs, name='about-us.home'),
    path('FAQ', views.FAQ, name='faq.home'),
]