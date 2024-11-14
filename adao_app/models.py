from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('candles', 'Candles'),
        ('clay', 'Clay')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name