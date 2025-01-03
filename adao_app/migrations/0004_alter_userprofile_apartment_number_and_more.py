# Generated by Django 5.1.3 on 2024-11-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adao_app', '0003_alter_userprofile_apartment_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='apartment_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='house_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='zip_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
