# Generated by Django 5.1.1 on 2024-09-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med_service', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=155, unique=True, verbose_name='продукт'),
        ),
    ]
