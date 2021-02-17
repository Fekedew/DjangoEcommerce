from django.contrib import admin
from .models import (
    Item, 
    OrderItem, 
    Order,
    CheckoutAddress,
    Payment,
    Category,
    Labels
)

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(CheckoutAddress)
admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(Labels)
