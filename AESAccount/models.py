from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user/avatar', null=True, blank=True, verbose_name='پروفایل')
    addr = models.TextField(null=True, blank=True, verbose_name='ادرس')
    phone = models.IntegerField(null=True, blank=True, verbose_name='شماره موبایل')
    email_verified = models.BooleanField(default=False, verbose_name='فعال بودن ایمیل')
    is_active = models.BooleanField(default=False, verbose_name='فعال بودن کاربر')
    is_delete = models.BooleanField(default=False, verbose_name='حذف کاربر')
    email_validation_code = models.CharField(null=True, blank=True, verbose_name='کد ایمیل', max_length=80)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
