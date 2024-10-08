# Generated by Django 5.1 on 2024-08-25 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AESProduct', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'محصول ها'},
        ),
        migrations.AlterModelOptions(
            name='product_brands',
            options={'verbose_name': 'برند', 'verbose_name_plural': 'برند ها'},
        ),
        migrations.AlterModelOptions(
            name='product_categories',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='product_comment',
            options={'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.AlterModelOptions(
            name='product_tags',
            options={'verbose_name': 'تگ', 'verbose_name_plural': 'تگ ها'},
        ),
        migrations.AlterModelOptions(
            name='products_gallery',
            options={'verbose_name': 'گالری', 'verbose_name_plural': 'گالری ها '},
        ),
        migrations.AlterModelOptions(
            name='products_sizes',
            options={'verbose_name': 'سایز', 'verbose_name_plural': 'سایز ها'},
        ),
        migrations.AlterField(
            model_name='product',
            name='new',
            field=models.BooleanField(default=False, verbose_name='جدید'),
        ),
        migrations.DeleteModel(
            name='Products_Colors',
        ),
    ]
