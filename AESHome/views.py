from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .forms import ContactUsForm
from .models import SiteSetting, Footer_Link_my_account, Footer_Link_info, InstaFeed, FooterFeatures


def index(request):
    return render(request, 'AESHome/index.html')


class Contact_Us(CreateView):
    template_name = 'AESHome/contact.html'
    form_class = ContactUsForm

    def get_success_url(self):
        return reverse('contact-us.home') + '?code=200&status=پیام شما با موفقیت ارسال شد'


def AboutUs(request):
    return render(request, 'AESHome/about.html')


def FAQ(request):
    return render(request, 'AESHome/faq.html')


def Footer(request):
    context = {
        'SiteSetting': SiteSetting.active.first(),
        'Footer_Link_my_account': Footer_Link_my_account.active.order_by('-id').all()[:6],
        'Footer_Link_info': Footer_Link_info.active.order_by('-id').all()[:6],
        'InstaFeed': InstaFeed.active.order_by('-id').all()[:9],
        'FooterFeatures': FooterFeatures.active.order_by('-id').all()[:4]

    }
    return render(request, 'Layouts/Footer/FooterBase.html', context)


def Header(request):
    context = {
        'SiteSetting': SiteSetting.active.first(),

    }
    return render(request, 'Layouts/Header/HeaderBase.html', context)
