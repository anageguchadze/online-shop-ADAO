from django.contrib import admin
from .models import Product

# Register your models here. admin - admin123
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')  # სურათის ჩვენება

admin.site.register(Product, ProductAdmin)