from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'category', 'price', 'for_sale')
    search_fields = ('name', 'code', 'category')
    list_filter = ('for_sale', 'category')
