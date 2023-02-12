from django.shortcuts import render
from .models import (
    Product, 
    Cart, 
    Order,
)
from ecommerce.serializer import (
    ProductSerializer, 
    CartSerializer, 
    OrderSerializer, 
)
from ecommerce.managers.cart_manager import CartManager
from ecommerce.managers.product_manager import ProductManager
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

class ProductViewSet(ViewSet):
    allowed_filters = [
        'name', 
        'name_rev', 
        'price', 
        'price_rev', 
        'score', 
        'score_rev', 
    ]
    @action(detail=False, methods=['GET'], url_path='list')
    def get_products_list(self, request):
        # default filter is higher score
        filter_by = request.data.get('filter_by', 'score')
        if filter_by not in self.allowed_filters:
            filter_by = 'score'
        manager = ProductManager()
        products_list = manager.get_products_list(filter_by)
        serialized_data = [ProductSerializer(product).data for product in products_list]
        return Response(
            data = serialized_data,
            status = status.HTTP_200_OK
        )


class CartViewSet(ViewSet):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'], url_path='active_cart')
    def get_active_cart_detail(self, request):
        user = request.user
        manager = CartManager(user)
        active_cart = manager.get_active_cart()
        return Response(
            data = CartSerializer(active_cart).data, 
            status = status.HTTP_200_OK
        )

    @action(detail=False, methods=['POST'], url_path='add_prod')
    def add_product_to_cart(self, request):
        user = request.user
        product_id = request.data.get('product_id', None)
        if not product_id:
            return Response(
                data = {"detail": "Missing product_id"}, 
                status = status.HTTP_400_BAD_REQUEST
            )
        all_products_ids = Product.objects.values_list('id', flat=True)
        if int(product_id) not in all_products_ids:
            return Response(
                data = {
                    "detail": "Product not found",
                    "requested_product": product_id,
                    "available_products": all_products_ids,
                }, 
                status = status.HTTP_400_BAD_REQUEST
            )
        manager = CartManager(user)
        manager.add_product(product_id)
        active_cart = manager.get_active_cart()
        return Response(
            data = CartSerializer(active_cart).data, 
            status = status.HTTP_200_OK
        )

    @action(detail=False, methods=['POST'], url_path='remove_prod')
    def remove_product_at_cart(self, request):
        user = request.user
        product_id = request.data.get('product_id', None)
        if not product_id:
            return Response(
                data = {"detail": "Missing product_id"}, 
                status = status.HTTP_400_BAD_REQUEST
            )
        manager = CartManager(user)
        active_cart = manager.get_active_cart()
        products_at_cart = active_cart.products_at_cart.values_list('product', flat=True)
        if int(product_id) not in products_at_cart:
            return Response(
                data = {
                    "detail": "Product not in cart",
                    "requested_product": product_id,
                    "available_products": products_at_cart,
                },
                status = status.HTTP_400_BAD_REQUEST
            )
        manager.remove_product(product_id)
        active_cart.refresh_from_db()
        return Response(
            data = CartSerializer(active_cart).data, 
            status = status.HTTP_200_OK
        )

    @action(detail=False, methods=['POST'], url_path='checkout')
    def checkout_cart(self, request):
        user = request.user
        manager = CartManager(user)
        active_cart = manager.get_active_cart()
        if active_cart.total_amount == 0:
            return Response(
                data = {
                    "detail": "Empty cart"
                },
                status = status.HTTP_400_BAD_REQUEST
            )
        order = manager.checkout_cart()
        return Response(
            data = OrderSerializer(order).data,
            status = status.HTTP_200_OK
        )

class OrderViewSet(ViewSet):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    @action(detail=False, methods=['GET'], url_path='list')
    def get_order_list(self, request):
        user = request.user
        order_list = Order.objects.filter(user=user).order_by('-date_checkout')
        serialized_data = [OrderSerializer(order).data for order in order_list]
        return Response(
            data=serialized_data, 
            status = status.HTTP_200_OK
        )