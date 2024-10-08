# Generated by Django 5.1 on 2024-08-28 17:34

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AESHome', '0003_alter_contact_us_sent_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('description2', models.TextField(verbose_name='قسمت دوم توضیحات')),
                ('team_active_posts', models.BooleanField(default=False, verbose_name='فعال کردن قسمت افراد')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف')),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'قسمت درباره ما',
            },
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='FAQS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('content', models.TextField(verbose_name='متن')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف')),
            ],
            options={
                'verbose_name': 'سوال پر تکرار',
                'verbose_name_plural': 'سوالات پر تکرار',
            },
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Footer_Link_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('url', models.URLField(verbose_name='لینک')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف')),
            ],
            options={
                'verbose_name': 'لینک  پایین صفحه بخش اینفو',
                'verbose_name_plural': 'لینک های پایین صفحه بخش اینفو',
            },
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Footer_Link_my_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('url', models.URLField(verbose_name='لینک')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف')),
            ],
            options={
                'verbose_name': 'لینک  پایین صفحه بخش مای اکانت',
                'verbose_name_plural': 'لینک های پایین صفحه مای اکانت',
            },
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='InstaFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='insta_feed/', verbose_name='عکس')),
                ('url', models.URLField(verbose_name='لینک')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف')),
            ],
            options={
                'verbose_name': 'لینک  پایین صفحه بخش اینستا',
                'verbose_name_plural': 'لینک های پایین صفحه بخش اینستا',
            },
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo', verbose_name='لوگوی سایت')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل ')),
                ('email2', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل دوم')),
                ('number', models.BigIntegerField(verbose_name='شماره')),
                ('number2', models.BigIntegerField(blank=True, null=True, verbose_name='شماره دوم')),
                ('short_desc', models.TextField(verbose_name='توضیحات کوتاه')),
                ('copyright', models.CharField(max_length=300, verbose_name='متن کپب رابت')),
                ('addr', models.CharField(max_length=300, verbose_name='ادرس خلاصه شده')),
                ('working_hours', models.CharField(max_length=300, verbose_name='ساعات کاری')),
                ('whatsapp_link', models.URLField(blank=True, null=True, verbose_name='لینک واتس اپ')),
                ('insta_link', models.URLField(blank=True, null=True, verbose_name='لینک اینستا')),
                ('twitter_link', models.URLField(blank=True, null=True, verbose_name='لینک تویتر')),
                ('linkin_link', models.URLField(blank=True, null=True, verbose_name='لینک لینک این')),
                ('telegram_url', models.URLField(blank=True, null=True, verbose_name='لینک تلگرام')),
                ('facebook_url', models.URLField(blank=True, null=True, verbose_name='لینک فیس بوک')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف')),
            ],
            options={
                'verbose_name': 'تنضیمات سایت',
                'verbose_name_plural': 'تنضیمات سایت',
            },
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='contact_us',
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='contact_us',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AddField(
            model_name='contact_us',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='حذف'),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='email',
            field=models.EmailField(max_length=200, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name='نام کامل'),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='message',
            field=models.TextField(verbose_name='پیام'),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='phone',
            field=models.IntegerField(verbose_name='شماره'),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='sent_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال'),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='status',
            field=models.BooleanField(default=False, verbose_name='وضعیت خوانده شده توسط مدیر'),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='subject',
            field=models.CharField(max_length=250, verbose_name='موضوع'),
        ),
        migrations.CreateModel(
            name='About_Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/teams', verbose_name='عکس')),
                ('full_name', models.CharField(max_length=200, verbose_name='نام کامل')),
                ('response', models.CharField(max_length=200, verbose_name='مسئولیت')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AESHome.about_us')),
            ],
            options={
                'verbose_name': 'قسمت فرد در صفحه تماس با ما',
                'verbose_name_plural': 'قسمت افراد در صفحه تماس با ما',
            },
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='About_Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/features', verbose_name='عکس')),
                ('title', models.CharField(max_length=75, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('url', models.URLField(verbose_name='لینک')),
                ('url_name', models.CharField(max_length=200, verbose_name='نام لینک')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AESHome.about_us', verbose_name='مربوط به توضیحات')),
            ],
            options={
                'verbose_name': 'ویژگی ما',
                'verbose_name_plural': 'ویژگی های ما',
            },
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='FooterFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عکس')),
                ('description', models.CharField(max_length=200, verbose_name='توضیحات')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف')),
                ('SiteSetting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AESHome.sitesetting', verbose_name='تنضیمات سایت')),
            ],
            options={
                'verbose_name': 'قسمت ویژگی اخر صفحه',
                'verbose_name_plural': 'قسمت های ویژگی اخر صفحه',
            },
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
    ]
