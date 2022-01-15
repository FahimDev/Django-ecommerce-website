# Generated by Django 4.0.1 on 2022-01-14 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_billingaddress_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='user',
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.customer'),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='status',
            field=models.CharField(choices=[(0, 'Optional Address'), (1, 'Current Delivery')], default=0, max_length=100),
        ),
    ]