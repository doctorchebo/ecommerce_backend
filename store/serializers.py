from rest_framework import serializers

from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product', 'name', 'image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(read_only=True, many=True)
    discount_price = serializers.ReadOnlyField()
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'long_description', 'points_value', 'sales_value', 'price', 'discount', 'discount_price', 'images']