from django.contrib import admin

from .models import Product
admin.site.site_title = "Shop Products Administration"
admin.site.site_header = "Shop Products Admin"
admin.site.index_title = "Welcome to Shop Products Admin"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'category', 'price', 'for_sale')
    search_fields = ('name', 'code', 'category')
    list_filter = ('for_sale', 'category')
    ordering = ('name', '-price')


