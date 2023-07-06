from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        )
    
    # As it's possible to sort by multiple fields, we need to create a tuple
    # To reverse the order, add a minus sign before the field name
    ordering = ('sku',) 
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        )
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
