from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False, is_active=True)


class Product_Tags(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان تگ')
    slug = models.CharField(max_length=100, verbose_name='نام در url (باید انگلیسی باشد)')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    products = models.ManyToManyField('Product', verbose_name='محصولات',
                                      related_name='tags')
    active = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class Product_Categories(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان کتگوری')
    slug = models.CharField(max_length=100, verbose_name='نام در url (باید انگلیسی باشد)')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    products = models.ManyToManyField('Product', verbose_name='محصولات'
                                      ,related_name='categories'
                                      )
    parent = models.ForeignKey('Product_Categories', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name='زیر مجموعه',
                               related_name='child'

                               )
    active = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product_Brands(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان برند')
    slug = models.CharField(max_length=100, verbose_name='نام در url (باید انگلیسی باشد)')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    products = models.ManyToManyField('Product', verbose_name='محصولات',
                                      related_name='brands'
                                      )

    def __str__(self):
        return self.title

    active = ProductManager()

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان محصول')
    description = models.TextField(verbose_name='توضیحات')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    price = models.IntegerField(verbose_name='قیمت')
    stock = models.IntegerField(verbose_name='موجودی')
    image = models.ImageField(upload_to='products/', verbose_name='عکس')
    rating = models.IntegerField(null=True, blank=True, default=0,
                                 validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='میانگین ریت ها')
    more_details = models.TextField(verbose_name='توضیحات اضافی', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ بروز رسانی')
    slug = models.SlugField(verbose_name='نام در url (باید انگلیسی باشد)')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    off = models.FloatField(null=True, blank=True, verbose_name='تخفیف',
                            validators=[MinValueValidator(0), MaxValueValidator(100)])
    new = models.BooleanField(default=False, verbose_name='جدید')
    has_size = models.BooleanField(default=False, verbose_name="داشتن سایز برای محصول")
    active = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصول ها'


class Products_Sizes(models.Model):
    size = models.CharField(max_length=100, verbose_name='سایز')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    active = ProductManager()

    def __str__(self):
        return f'{self.product.title} {self.size}'

    class Meta:
        verbose_name = 'سایز'
        verbose_name_plural = 'سایز ها'


class Products_Gallery(models.Model):
    image = models.ImageField(upload_to='products/gallery', verbose_name='عکس')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول',
                                related_name='gallery'
                                )
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    active = ProductManager()

    def __str__(self):
        return f'{self.product.title} {self.id}'

    active = ProductManager()

    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری ها '


class Product_comment(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='نام')
    email = models.EmailField(max_length=150, verbose_name='ایمیل')
    comment = models.TextField(verbose_name='کامنت')
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='ریت')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول'
                                ,related_name='comments'
                                )
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               related_name='child',
                               )
    active = ProductManager()
    objects = models.Manager()

    def __str__(self):
        return f'{self.product.title} {self.full_name}'

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
