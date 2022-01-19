# Generated by Django 3.2.11 on 2022-01-19 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_rename_product_id_productimage_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='product_id',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product_img_src',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=''),
        ),
    ]
