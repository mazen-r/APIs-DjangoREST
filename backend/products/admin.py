from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'price']

admin.site.register(Product, ProductAdmin)