from django.db import models
from django.contrib.auth.models import User

from .constants import StatusChoices


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField()

    def __str__(self):
        return '%s' % (self.id)

    class Meta:
        db_table = "cart"


class ProductInCart(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = "product_in_cart"
        unique_together = (("cart", "product"),)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=256, choices=StatusChoices.choices, default=StatusChoices.NOT_PACKED
    )

    class Meta:
        db_table = "order"
