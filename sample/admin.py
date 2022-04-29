from django.contrib import admin

from .models import Cart, Product, ProductInCart, Order

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(ProductInCart)
admin.site.register(Order)
