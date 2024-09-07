from django.urls import path

from . import views

urlpatterns = [
    path('', views.Dashboard, name='Dashboard.account'),
    path('send-email/', views.Email_verification_send_mail, name='send.email.account'),
    path('email-verified/<str:code>', views.Email_verification_from_email, name='verified.email.account'),
    path('authentication', views.Authentication, name='Authentication.account'),
    path('authentication/activate-account/<str:code>', views.active_account, name='Authentication.activate.account'),
    path('authentication/login', views.Authentication_login, name='Authentication.login.account'),
    path('authentication/register', views.Authentication_register, name='Authentication.register.account'),
    path('authentication/logout', views.Authentication_logout, name='Authentication.logout.account'),
    path('UserEditProfile/', views.UserEditProfile_from, name='UserEditProfile_from.account'),
    path('UserDetailOrder-show/<int:oid>', views.UserDetailOrder_show, name='UserDetailOrder.account'),
    path('user-change-pass', views.change_pss, name='user-change-pass'),
]
