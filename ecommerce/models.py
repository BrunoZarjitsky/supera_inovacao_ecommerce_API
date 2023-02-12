from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(_("Name"), max_length=124, default="")
    price = models.FloatField(_("Price"), default=0)
    score = models.IntegerField(_("Score"), default=0)
    image = models.ImageField(_("Image"), upload_to="media/product_images/")

    def __str__(self):
        return self.name

class ProductAtCart(models.Model):
    cart_id = models.IntegerField()
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    product_name = models.CharField(_("Name"), max_length=124, default="")

    def __str__(self):
        return f"{self.cart_id} {self.product_name}"

class Cart(models.Model):
    user = models.ForeignKey(
        to = User, 
        verbose_name = _("Cart owner"), 
        on_delete = models.CASCADE,
        null = False, 
        blank = False
    )
    products_at_cart = models.ManyToManyField(ProductAtCart, related_name='products', verbose_name=_("Products"), blank=True)
    products_amount = models.FloatField(verbose_name = _("Products amount"), default=0)
    delivery_amount = models.FloatField(verbose_name = _("Delivery amount"), default=0)
    total_amount = models.FloatField(verbose_name = _("Total amount"), default=0)
    active = models.BooleanField(_("Is active"), default = True)

class Order(models.Model):
    user = models.ForeignKey(
        to = User, 
        verbose_name = _("User"), 
        on_delete = models.CASCADE,
        null = False, 
        blank = False
    )
    cart = models.ForeignKey(
        to = Cart,
        verbose_name = _("Products"),
        on_delete = models.CASCADE,
        null = False,
        blank = True,
    )
    date_checkout = models.DateField(_("Date of checkout"), auto_now=False, auto_now_add=False)