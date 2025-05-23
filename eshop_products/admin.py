from django.contrib import admin

# Register your models here.

from .models import Product, ProductGallery


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'active', 'price']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
