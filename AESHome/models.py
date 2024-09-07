from django.db import models


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False, is_active=True).all()


class SiteSetting(models.Model):
    logo = models.ImageField(upload_to='logo', verbose_name='لوگوی سایت')
    title = models.CharField(max_length=50, verbose_name='عنوان')
    email = models.EmailField(verbose_name='ایمیل ')
    email2 = models.EmailField(verbose_name='ایمیل دوم', null=True, blank=True)
    number = models.BigIntegerField(verbose_name='شماره')
    number2 = models.BigIntegerField(verbose_name='شماره دوم', null=True, blank=True)
    short_desc = models.TextField(verbose_name='توضیحات کوتاه')
    copyright = models.CharField(max_length=300, verbose_name='متن کپب رابت')
    addr = models.CharField(max_length=300, verbose_name='ادرس خلاصه شده')
    working_hours = models.CharField(max_length=300, verbose_name='ساعات کاری')
    whatsapp_link = models.URLField(null=True, blank=True, verbose_name='لینک واتس اپ')
    insta_link = models.URLField(null=True, blank=True, verbose_name='لینک اینستا')
    twitter_link = models.URLField(null=True, blank=True, verbose_name='لینک تویتر')
    linkin_link = models.URLField(null=True, blank=True, verbose_name='لینک لینک این')
    telegram_url = models.URLField(null=True, blank=True, verbose_name='لینک تلگرام')
    facebook_url = models.URLField(null=True, blank=True, verbose_name='لینک فیس بوک')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    active = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تنضیمات سایت'
        verbose_name_plural = 'تنضیمات سایت'


class Footer_Link_my_account(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url = models.URLField(verbose_name='لینک')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    active = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'لینک  پایین صفحه بخش مای اکانت'
        verbose_name_plural = 'لینک های پایین صفحه مای اکانت'


class Footer_Link_info(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url = models.URLField(verbose_name='لینک')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    active = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'لینک  پایین صفحه بخش اینفو'
        verbose_name_plural = 'لینک های پایین صفحه بخش اینفو'


class InstaFeed(models.Model):
    image = models.ImageField(upload_to='insta_feed/', verbose_name='عکس')
    url = models.URLField(verbose_name='لینک')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    active = ProductManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'لینک  پایین صفحه بخش اینستا'
        verbose_name_plural = 'لینک های پایین صفحه بخش اینستا'


class FooterFeatures(models.Model):
    title = models.CharField(max_length=200, verbose_name='عکس')
    description = models.CharField(max_length=200, verbose_name='توضیحات')
    SiteSetting = models.ForeignKey(SiteSetting, on_delete=models.CASCADE, verbose_name='تنضیمات سایت')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    active = ProductManager()
    objects = models.Manager()

    def __str__(self):
        return self.title + '  ' + self.SiteSetting.title

    class Meta:
        verbose_name = 'قسمت ویژگی اخر صفحه'
        verbose_name_plural = 'قسمت های ویژگی اخر صفحه'


class Contact_us(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='نام کامل')
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    phone = models.IntegerField(verbose_name='شماره')
    subject = models.CharField(max_length=250, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')
    status = models.BooleanField(default=False, verbose_name='وضعیت خوانده شده توسط مدیر')
    sent_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    active = ProductManager()

    def __str__(self):
        return self.full_name + '>>' + self.subject

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'


class About_us(models.Model):
    small_title = models.CharField(max_length=75, verbose_name='متن بالای عنوان')
    title = models.CharField(max_length=75, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    description2 = models.TextField(verbose_name='قسمت دوم توضیحات')
    team_active_posts = models.BooleanField(default=False, verbose_name='فعال کردن قسمت افراد')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    active = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'قسمت درباره ما'


class About_Team(models.Model):
    image = models.ImageField(upload_to='about/teams', verbose_name='عکس')
    full_name = models.CharField(max_length=200, verbose_name='نام کامل')
    response = models.CharField(max_length=200, verbose_name='مسئولیت')
    linkin_url = models.URLField(verbose_name='لینک این', null=True, blank=True)
    telegram_url = models.URLField(verbose_name='لینک تلگرام', null=True, blank=True)
    costume_url = models.URLField(verbose_name='لینک های دیگر', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    about = models.ForeignKey(About_us, on_delete=models.CASCADE)
    active = ProductManager()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'قسمت فرد در صفحه تماس با ما'
        verbose_name_plural = 'قسمت افراد در صفحه تماس با ما'


class About_Features(models.Model):
    image = models.ImageField(upload_to='about/features', verbose_name='عکس')
    title = models.CharField(max_length=75, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    url = models.URLField(max_length=200, verbose_name='لینک')
    url_name = models.CharField(max_length=200, verbose_name='نام لینک')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    about = models.ForeignKey(About_us, on_delete=models.CASCADE, verbose_name='مربوط به توضیحات')
    sub_title = models.CharField(max_length=75, verbose_name='بالای عنوان')
    active = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ویژگی ما'
        verbose_name_plural = 'ویژگی های ما'


class FAQS(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    content = models.TextField(verbose_name='متن')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    active = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'سوال پر تکرار'
        verbose_name_plural = 'سوالات پر تکرار'


class RedLine(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    link_title = models.CharField(max_length=200, verbose_name='نام لینک')
    link = models.URLField(verbose_name='لینک')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    active = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'لینک بالا صفحه(خط قرمز قرمز)'
        verbose_name_plural = 'لینک های بالا صفحه(خط قرمز قرمز)'
