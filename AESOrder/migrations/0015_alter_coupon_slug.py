# Generated by Django 5.1 on 2024-09-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AESOrder', '0014_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='نام در لینک حتما باید انگلیسی باشد'),
        ),
    ]
