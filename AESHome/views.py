from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .forms import ContactUsForm


# Create your views here.

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
    return render(request, 'Layouts/Footer/FooterBase.html')
