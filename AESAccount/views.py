from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, reverse
from django.utils.crypto import get_random_string

from AESOrder.models import OrderDetail, Order
from .forms import UserLoginForm, UserRegisterForm, EditAddrForm, UserEditProfile
from .models import User


@login_required
def Dashboard(request):
    status_red = None
    user = User.objects.filter(id=request.user.id, is_active=True, is_delete=False,
                               email__iexact=request.user.email,
                               username__iexact=request.user.username
                               ).first()
    order: Order = Order.active.get_or_create(user=user)[0]
    if request.method == 'POST':
        form = EditAddrForm(request.POST)
        if form.is_valid():
            addr = form.cleaned_data['addr']
            post = form.cleaned_data['post']
            if user is not None:
                if user.is_active or not user.is_delete or user.email_verified:
                    if addr is not None and post is not None:
                        user.addr = addr
                        user.post = post
                        user.save()
                        status_red = 200
                    else:
                        form.add_error(addr, 'لطفا اطلاعات خواسته شده را به درستی وارد فرمایید')
                        form.add_error(post, 'لطفا اطلاعات خواسته شده را به درستی وارد فرمایید')
                else:
                    status_red = 'لطفا حساب کاربری خود را فعال کنید'
        else:
            status_red = 'لطفا اطلاعات خواسته شده را به درستی وارد فرمایید'

    context = {'user': user,
               'EditAddrForm': EditAddrForm(initial={
                   'addr': user.addr,
                   'post': user.post
               }),
               'status_red': status_red,
               'UserEditProfile': UserEditProfile(instance=user),
               'order_c': order,
               'order_last': Order.objects.filter(is_active=True, is_paid=True, user=request.user).order_by('-id').all(),
               }
    return render(request, 'AESAccount/account.html', context)


@login_required
def UserEditProfile_from(request):
    if request.method == 'POST':
        curren_user = User.objects.filter(id=request.user.id, is_active=True, is_delete=False,
                                          email__iexact=request.user.email,
                                          username__iexact=request.user.username
                                          ).first()
        form = UserEditProfile(request.POST, request.FILES, instance=curren_user)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('Dashboard.account') + '?status=اطلاعات شما با موفقیت ویرایش شد&code=200')
        else:
            return redirect(reverse('Dashboard.account') + '?status=مشکلی پیش امده است&code=0')


def Email_verification_send_mail(request):
    pass


def Email_verification_from_email(request):
    pass


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
                status = '?status=(نام کاربری باید با زبان انگلیسی و اعداد باشد) کاربر موجود می باشد یا نام کاربری موجود می باشد&code=1'
                return redirect(reverse('Authentication.account') + status)
            elif user is None:
                new_user = User.objects.create(username=username, email=email,
                                               email_validation_code=get_random_string(80))
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


@login_required
def UserDetailOrder_show(request, oid):
    order: Order = Order.objects.prefetch_related('details').filter(user=request.user ,id=int(oid), is_active=True).first()
    if order is None:
        return Http404()
    # print(order.details.all())
    context = {
        # 'orders': OrderDetail.objects.filter(order__id=int(oid), order__user=request.user, is_active=True, order__is_active=True).all(),
        'orders': order.details.all(),
    }
    print(context)
    return render(request, 'AESAccount/order-details.html', context)
