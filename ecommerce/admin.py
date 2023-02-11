from django.contrib import admin
from .models import Product, Cart, Order

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    fields = [
        'name', 
        'price', 
        'score', 
        'image', 
    ]
    list_display = [
        'name', 
        'price', 
        'score',
    ]
    list_filter = [
        'name',
    ]

admin.site.register(Product, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    fields = [
        'user', 
        'products', 
        'products_amount', 
        'delivery_amount', 
        'total_amount', 
        'active', 
    ]
    list_display = [
        'user', 
        'total_amount', 
        'active', 
    ]
    list_filter = [
        'user', 
        'active',
    ]

admin.site.register(Cart, CartAdmin)

class OrderAdmin(admin.ModelAdmin):
    fields = [
        'user', 
        'cart', 
        'date_checkout', 
    ]
    list_display = [
        'user', 
        'cart', 
        'date_checkout', 
    ]
    list_filter = [
        'user',
        'date_checkout',
    ]

admin.site.register(Order, OrderAdmin)