from ecommerce.models import (
    Product, 
    Cart, 
    Order,
)
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'price', 
            'score', 
        ]

class CartSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    products_at_cart = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = [
            'id', 
            'user', 
            'products_at_cart', 
            'products_amount', 
            'delivery_amount', 
            'total_amount', 
            'active', 
        ]

    def get_products_at_cart(self, instance):
        return instance.products_at_cart.values_list('product_name', flat=True)

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    cart = serializers.ReadOnlyField(source='cart.id')
    class Meta:
        model = Order
        fields = [
            'id', 
            'user', 
            'cart', 
            'date_checkout', 
        ]