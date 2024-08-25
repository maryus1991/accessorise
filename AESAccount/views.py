from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from django.utils.crypto import get_random_string

from .forms import UserLoginForm, UserRegisterForm
from .models import User


@login_required
def Dashboard(request):
    return render(request, 'AESAccount/account.html')


def Authentication(request):
    UserLoginForm_context = UserLoginForm()
    UserRegisterForm_context = UserRegisterForm()
    con = {
        'UserLoginForm': UserLoginForm_context,
        'UserRegisterForm': UserRegisterForm_context
    }
    return render(request, 'AESAccount/login.html', con)


def Authentication_login(request):
    if request.method == 'POST':
        UserLoginForm_context = UserLoginForm(request.POST)
        if UserLoginForm_context.is_valid():
            user: User = User.objects.filter(email__iexact=UserLoginForm_context.cleaned_data.get('email'),
                                             is_delete=False).first()
            if user is not None:
                if user.check_password(UserLoginForm_context.cleaned_data.get('password')):
                    if user.is_active and user.email_verified:
                        login(request, user)
                        # todo send email
                        status = '?status=خوش آمدید&code=200'
                        return redirect(reverse('Dashboard.account') + status)
                    else:
                        status = '?status=کاربر شما فعال نمی باشد&code=0'
                else:
                    status = '?status=اطلاعات شما درست نمی باشد&code=0'
            else:
                status = '?status=اطلاعات شما درست نمی باشد&code=0'
        else:
            status = '?status=اطلاعات شما درست نمی باشد&code=0'
    else:
        status = '?status=مشکلی پیش امده است&code=0'
    return redirect(reverse('Authentication.account') + status)


@login_required
def Authentication_logout(request):
    logout(request)
    return redirect(reverse('Authentication.account'))


def Authentication_register(request):
    if request.method == 'POST':
        UserRegisterForm_context = UserRegisterForm(request.POST)
        if UserRegisterForm_context.is_valid():
            username = UserRegisterForm_context.cleaned_data.get('username')
            email = UserRegisterForm_context.cleaned_data.get('email')
            user: User = User.objects.filter(Q(username=username) | Q(email=email), is_delete=False).first()
            if user is not None:
                status = '?status= کاربر موجود می باشد یا نام کاربری موجود می باشد&code=1'
                return redirect(reverse('Authentication.account') + status)
            elif user is None:
                new_user = User.objects.create(username=username, email=email, email_validation_code=get_random_string(80))
                new_user.set_password(UserRegisterForm_context.cleaned_data.get('password'))
                # todo : send email
                new_user.save()
                status = '?status=یک ایمیل برایتان ارسال شد است (پوشه اسپم یا هرزنامه را هم چک کنید) لطفا ان را فعال کنید و سپس وارد شود کنید &code=1'
            else:
                status = '?status=مشکلی پیش امده است&code=0'
        else:
            status = '?status= کاربر موجود می باشد یا نام کاربری موجود می باشد&code=1'
    else:
        status = '?status=مشکلی پیش امده است&code=0'
    return redirect(reverse('Authentication.account') + status)
