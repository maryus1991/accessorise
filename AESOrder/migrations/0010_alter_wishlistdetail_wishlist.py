# Generated by Django 5.1 on 2024-09-04 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AESOrder', '0009_alter_wishlistdetail_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistdetail',
            name='wishlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='AESOrder.order', verbose_name='محصول مورد علاقه'),
        ),
    ]
