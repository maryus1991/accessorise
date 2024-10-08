# Generated by Django 5.1 on 2024-09-05 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AESOrder', '0015_alter_coupon_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_complete',
            field=models.BooleanField(default=False, verbose_name='تکمیل توسط کاربر'),
        ),
        migrations.AddField(
            model_name='order',
            name='send_price',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='قیمت ارسال'),
        ),
    ]
