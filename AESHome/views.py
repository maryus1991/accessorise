from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from AESUtils.lists_maker import lists_maker
from .forms import ContactUsForm
from .models import SiteSetting, Footer_Link_my_account, Footer_Link_info, InstaFeed, FooterFeatures, FAQS, About_us
from AESOrder.models import Order, WishList, WishListDetail

def index(request):
    return render(request, 'AESHome/index.html')


class Contact_Us(CreateView):
    template_name = 'AESHome/contact.html'
    form_class = ContactUsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SiteSetting'] = SiteSetting.active.order_by('-id').first()
        return context

    def get_success_url(self):
        return reverse('contact-us.home') + '?code=200&status=پیام شما با موفقیت ارسال شد'


def AboutUs(request):
    context = {'SiteSetting': SiteSetting.active.first(),
               'About_us': About_us.active.prefetch_related('about_team_set', 'about_features_set').order_by(
                   '-id').first(),

               }
    return render(request, 'AESHome/about.html', context)


def FAQ(request):
    con = {'FAQS': lists_maker(list(FAQS.active.order_by('-id').all()))}

    return render(request, 'AESHome/faq.html', con)


def Footer(request):
    context = {'SiteSetting': SiteSetting.active.first(),
               'Footer_Link_my_account': Footer_Link_my_account.active.order_by('-id').all()[:6],
               'Footer_Link_info': Footer_Link_info.active.order_by('-id').all()[:6],
               'InstaFeed': InstaFeed.active.order_by('-id').all()[:9],
               'FooterFeatures': FooterFeatures.active.order_by('-id').all()[:4]

               }
    return render(request, 'Layouts/Footer/FooterBase.html', context)


def Header(request):
    try:
        order:Order = Order.active.filter(user=request.user).first()
        OrderList = order.details
        WishList_ = WishListDetail.active.filter(wishlist__user=request.user, wishlist__is_active=True
                                                 ,wishlist__is_delete=False)
    except:
        OrderList = 0
        WishList_ = 0
    context = {
        'SiteSetting': SiteSetting.active.first(),
        'OrderList': OrderList,
        'WishList': WishList_
    }
    return render(request, 'Layouts/Header/HeaderBase.html', context)
