from django.contrib import admin
from .models import Product, Category, Review, ProductImage

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'calculate_average_rating',
        'price',
        'image',
    )

    ordering = ('sku',)
    inlines = [ProductImageAdmin]  

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)