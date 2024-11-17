from django.contrib import admin
from .models import Product

# Register your models here. adaoadmin - candle
# on site email-ana@test.com - Santeli1234@
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')  # სურათის ჩვენება

admin.site.register(Product, ProductAdmin)