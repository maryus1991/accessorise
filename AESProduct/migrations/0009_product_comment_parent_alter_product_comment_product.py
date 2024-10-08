# Generated by Django 5.1 on 2024-09-03 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AESProduct', '0008_alter_product_brands_products_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='AESProduct.product_comment'),
        ),
        migrations.AlterField(
            model_name='product_comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='AESProduct.product', verbose_name='محصول'),
        ),
    ]
