from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

settings.configure()


def SendMail(to, subject, context, template_name):
    try:
        html_message = render_to_string(template_name, context)
        plain_message = strip_tags(html_message)
        send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [to], html_message=html_message)
        return True
    except:
        return False


send_mail('test', 'test', settings.EMAIL_HOST_USER, ['maryus19915123@gmail.com'])
