from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from AESAccount.models import User
from AESProduct.models import Product


class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, is_paid=False, is_complete=False)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='کاربر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساختن')
    is_active = models.BooleanField(default=True, verbose_name='فعال بودن')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده')
    payment_code = models.CharField(max_length=100, verbose_name='کد پرداخت', null=True, blank=True, )
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')
    total_price = models.BigIntegerField(default=0, verbose_name='قیمت نهایی کل')

    send_price = models.BigIntegerField(null=True, blank=True, verbose_name='قیمت ارسال')
    is_complete = models.BooleanField(default=False, verbose_name='تکمیل توسط کاربر') # for send to admin

    active = OrderManager()

    def __str__(self):
        return f'{self.pk} {self.user.username}'

    def get_final_price(self):
        total_price = 0
        # count = self.details.count()
        # if count > 0:
        if self.is_paid:
            for detail in self.details.all():
                total_price += detail.FinalPrice * detail.count
        else:
            for detail in self.details.all():
                if detail.product.off is not None or int(detail.product.off if detail.product.off is not None else 0) > 0:
                    total_price += (detail.product.price * (1 - (detail.product.off/100) )) * detail.count
                else:
                    total_price += detail.product.price * detail.count

        return total_price

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'


class OrderDetailManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details', verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orderDetails', verbose_name='محصول')
    FinalPrice = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی')
    count = models.IntegerField(null=True, blank=True, verbose_name='تعداد')
    size = models.CharField(max_length=100, null=True, blank=True, verbose_name='سایز')
    is_active = models.BooleanField(default=True, verbose_name='فعال بودن')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساختن')

    active = OrderDetailManager()

    def __str__(self):
        return f'{self.pk} {self.order.user.username}'

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'جزییات سبد های خرید'


class WishListManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, is_delete=False)


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='WishList', verbose_name='کاربر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساختن')
    is_active = models.BooleanField(default=True, verbose_name='فعال بودن')
    is_delete = models.BooleanField(default=False, verbose_name='حذف کردن')
    updated = models.DateTimeField(verbose_name='زمان اپدیت کردن', null=True, blank=True)
    active = WishListManager()

    def __str__(self):
        return f'{self.pk} {self.user.username}'

    class Meta:
        verbose_name = 'محصول مورد علاقه'
        verbose_name_plural = 'محصولات مورد علاقه'


class WishListDetailManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, is_delete=False)


class WishListDetail(models.Model):
    wishlist = models.ForeignKey(WishList, related_name='details', on_delete=models.CASCADE,
                                 verbose_name='محصول مورد علاقه')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='WishListDetail', verbose_name='محصول')
    is_active = models.BooleanField(default=True, verbose_name='فعال بودن')
    is_delete = models.BooleanField(default=False, verbose_name='حذف کردن')

    active = WishListDetailManager()

    def __str__(self):
        return f'{self.pk} {self.wishlist.user.username}'

    class Meta:
        verbose_name = 'جزییات محصول مورد علاقه'
        verbose_name_plural = 'جزییات محصولات مورد علاقه'


class CouponManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, is_delete=False)


class Coupon(models.Model):
    slug = models.SlugField(verbose_name='نام در لینک حتما باید انگلیسی باشد', unique=True)
    title = models.CharField(max_length=100, verbose_name='عنوان')
    off_percent = models.FloatField(validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ], verbose_name='مقدار تخفیف (درصدی)'
        , null=True, blank=True)
    off_tomman = models.IntegerField(
        verbose_name='مقدار تخفیف (تومان)'
        , null=True, blank=True)

    number = models.IntegerField(verbose_name='دفعات استفاده')
    number_by_user = models.IntegerField(verbose_name='دفعات استفاده برای هر کاربر', default=1)
    is_active = models.BooleanField(default=True, verbose_name='فعال بودن')
    is_delete = models.BooleanField(default=False, verbose_name='حذف کردن')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, )
    active = CouponManager()

    def __str__(self):
        return f'{self.title} {self.number}'

    # def save(self):
    #     if self.off_percent == 0:
    #         self.off_percent = None
    #     if self.off_tomman == 0:
    #         self.off_tomman = None
    #     return self


    class Meta:
        verbose_name_plural = 'کد های تخفیف'
        verbose_name = 'کد تخفیف'
