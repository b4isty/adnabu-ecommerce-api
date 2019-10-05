from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, m2m_changed
# Create your models here.


class Category(models.Model):
    """
    Model for Category
    """
    name = models.CharField(max_length=150, blank=False, null=False)
    total = models.DecimalField(decimal_places=2, blank=True, max_digits=50, default=0.00)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """
    Model for SubCategory
    """
    name = models.CharField(max_length=150, blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model for Product
    """
    title = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=30, default=0.00)
    in_stock_qty = models.IntegerField(default=0)
    out_of_stock = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True, related_name="products")
    sub_categories = models.ManyToManyField(SubCategory, blank=True, related_name='products')
    timestamp = models.DateTimeField(auto_now_add=True)


@receiver(pre_save, sender=Product)
def modify_out_of_stock(sender, instance, *args, **kwargs):
    """
    pre_save signal to modify the out of stock field
    if in_stock_qty exists
    """
    if instance.in_stock_qty:
        instance.out_of_stock = False


@receiver(m2m_changed, sender=Product.categories.through)
def update_category_total(instance, action, sender, *args, **kwargs):
    """
    m2m_changed signal to update category total
    """
    if action == "post_add" or action == "post_remove" or action == "post_clear":
        for category in instance.categories.all():
            category.total += instance.price*instance.in_stock_qty
            category.save()


