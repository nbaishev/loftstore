from django.contrib import admin

from .models import Order, ProductsInOrder


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'total_cost',)
    search_fields = ('user',)
    list_filter = ('created_at',)
    empty_value_display = '-пусто-'


@admin.register(ProductsInOrder)
class ProductsInOrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'order', 'quantity',)
    empty_value_display = '-пусто-'
