from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from products.models import Product

User = get_user_model()


class Cart(models.Model):
    """
    Model for Cart
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    products = models.ManyToManyField(Product, blank=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=25, default=0.00)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Order(models.Model):
    """
    Model for Order
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(m2m_changed, sender=Cart.products.through)
def update_cart_total_price(instance, action, sender, *args, **kwargs):
    """
    m2m_changed signal to update total price
    """
    if action == "post_add" or action == "post_remove" or action == "post_clear":
        total = 0
        product_qs = instance.products.all()
        for product in product_qs:
            total += product.price
        instance.total_price = total
        instance.save()


@receiver(post_save, sender=Order)
def update_order_total(sender, instance, *args, **kwargs):
    """
    post_save signal to update order total
    """
    if not instance.total:
        instance.total = instance.cart.total_price
        instance.save()

