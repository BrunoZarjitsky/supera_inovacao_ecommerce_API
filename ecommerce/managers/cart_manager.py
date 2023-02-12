from ecommerce.models import (
    Cart,
    Product,
    ProductAtCart,
    Order
)
from django.contrib.auth.models import User
from django.utils import timezone

class CartManager:
    def __init__(self, user:User):
        self.user = user

    def get_active_cart(self)-> Cart:
        active_cart = Cart.objects.filter(user = self.user, active = True).last()
        if not active_cart:
            active_cart = Cart.objects.create(
                user = self.user
            )
        self.update_total_amount(active_cart)
        return active_cart

    def deactive_cart(self)-> None:
        active_cart = self.get_active_cart()
        active_cart.active = False
        active_cart.save(update_fields=['active'])

    def add_product(self, product_id: int)-> None:
        product_instance = Product.objects.get(id = product_id)
        active_cart = self.get_active_cart()
        product_at_cart = ProductAtCart.objects.create(
            cart_id = active_cart.id, 
            product = product_instance,
            product_name = product_instance.name
        )
        active_cart.products_at_cart.add(product_at_cart)
        active_cart.products_amount += product_instance.price
        active_cart.save(update_fields=['products_amount'])
        self.update_total_amount(active_cart)

    def remove_product(self, product_id: int)-> None:
        active_cart = self.get_active_cart()
        product_at_cart = active_cart.products_at_cart.filter(product_id=product_id).first()
        active_cart.products_at_cart.remove(product_at_cart)
        active_cart.products_amount -= product_at_cart.product.price
        active_cart.save(update_fields=['products_amount'])
        self.update_total_amount(active_cart)

    def update_total_amount(self, active_cart: Cart)-> None:
        active_cart.delivery_amount = active_cart.products_at_cart.count() * 10
        if active_cart.products_amount >= 250:
            active_cart.delivery_amount = 0
        active_cart.total_amount = active_cart.products_amount + active_cart.delivery_amount
        active_cart.save(update_fields=['delivery_amount', 'total_amount'])
        
    def checkout_cart(self)-> Order:
        active_cart = self.get_active_cart()
        order = Order.objects.create(
            user = self.user,
            cart = active_cart,
            date_checkout = timezone.now().date()
        )
        active_cart.active = False
        active_cart.save(update_fields=['active'])
        return order