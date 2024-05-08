from django.db import models
from django.utils import timezone


class Product(models.Model):
    name= models.CharField(max_length=255, null=True, blank=True)
    slug=models.SlugField(max_length=255, null=True, blank=True)
    description= models.CharField(max_length=255, null=True, blank=True)
    long_description= models.TextField(max_length=3000, null=True, blank=True)
    points_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sales_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price= models.BigIntegerField(null=True, blank=True)
    discount= models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'
    
    @property
    def discount_price(self):
        if self.discount:
            return self.price * (1-self.discount)
        else:
            return self.price

class ProductImage(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    image= models.ImageField(upload_to='media/images', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.created_at}'