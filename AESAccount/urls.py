from django.urls import path

from . import views

urlpatterns = [
    path('', views.Dashboard, name='Dashboard.account'),
    path('authentication', views.Authentication, name='Authentication.account'),
    # path('authentication/login', views.Authentication, name='Authentication.account'),
    # path('authentication/register', views.Authentication, name='Authentication.account'),
    # path('authentication/logout', views.Authentication, name='Authentication.account'),
]
