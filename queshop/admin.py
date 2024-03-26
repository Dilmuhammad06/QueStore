from django.contrib import admin
from .models import Products, Coupon_code, Order, OrderItem


class AdminProducts(admin.ModelAdmin):
    listings = ['name','description','price','category','image']
admin.site.register(Products,AdminProducts)
admin.site.register([Coupon_code,Order,OrderItem])