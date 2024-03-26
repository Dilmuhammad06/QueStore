from django.db import models
from users.models import User

class Products(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    category = models.CharField(max_length=40)
    is_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_id = models.CharField(max_length=255)
    total_price = models.IntegerField()
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} ordered {self.order_id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} - {self.quantity}'
class Coupon_code(models.Model):
    code = models.CharField(max_length=7)
    sale = models.IntegerField()
    used = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.code} makes {self.sale}% sale'