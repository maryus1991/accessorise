# Generated by Django 5.1 on 2024-09-04 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AESOrder', '0010_alter_wishlistdetail_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistdetail',
            name='wishlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='AESOrder.wishlist', verbose_name='محصول مورد علاقه'),
        ),
    ]
