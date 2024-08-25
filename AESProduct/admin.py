from django.contrib import admin
from .models import (Product_Tags,
                     Product_Categories,
                     Product_Brands,
                     Product,
                     Products_Sizes,
                     Products_Gallery,
                     Product_comment)

# Register your models here.

admin.site.register(Product_Tags)
admin.site.register(Product_Categories)
admin.site.register(Product_Brands)
admin.site.register(Product)
admin.site.register(Products_Sizes)
admin.site.register(Products_Gallery)
admin.site.register(Product_comment)