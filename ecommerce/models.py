from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(_("Name"), max_length=124)
    price = models.FloatField(_("Price"))
    score = models.IntegerField(_("Score"))
    image = models.ImageField(_("Image"), upload_to="media/product_images/")

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(
        to = User, 
        verbose_name = _("Cart owner"), 
        on_delete = models.CASCADE,
        null = False, 
        blank = False
    )
    products = models.ManyToManyField(Product, verbose_name=_("Products"))
    products_amount = models.FloatField(verbose_name = _("Products amount"))
    delivery_amount = models.FloatField(verbose_name = _("Delivery amount"))
    total_amount = models.FloatField(verbose_name = _("Total amount"))
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