from django.urls import path

from . import views

urlpatterns = [
    path('', views.Dashboard, name='Dashboard.account'),
    path('authentication', views.Authentication, name='Authentication.account'),
    path('authentication/login', views.Authentication_login, name='Authentication.login.account'),
    path('authentication/register', views.Authentication_register, name='Authentication.register.account'),
    path('authentication/logout', views.Authentication_logout, name='Authentication.logout.account'),
]
