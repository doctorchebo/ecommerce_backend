from django.contrib import admin
from .models import Product, ProductImage

class ImageAdminInline(admin.TabularInline):
    model = ProductImage
    fields = ['product', 'image']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ImageAdminInline]
