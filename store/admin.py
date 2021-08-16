from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(m_Product)
admin.site.register(Prescription)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
# admin.site.register(Customer)