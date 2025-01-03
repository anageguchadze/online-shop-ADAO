# Generated by Django 5.1.3 on 2024-11-17 11:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adao_app', '0009_cart_favourite'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('user', 'product')},
        ),
        migrations.AlterUniqueTogether(
            name='favourite',
            unique_together={('user', 'product')},
        ),
    ]
