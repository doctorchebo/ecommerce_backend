from django.contrib import admin

from .filters import PointsValueListFilter
from .models import Product, ProductImage


class ImageAdminInline(admin.TabularInline):
    model = ProductImage
    fields = ['product', 'image']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "get_discount", "discount_price", "points_value", "sales_value"]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = [PointsValueListFilter]
    inlines = [ImageAdminInline]
    ordering = ["name"]

    def get_discount(self, obj):
        return f'{obj.discount * 100}%'
