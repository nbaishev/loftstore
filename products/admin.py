from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'category', 'price',)
    search_fields = ('name',)
    list_filter = ('category',)
    empty_value_display = '-пусто-'
