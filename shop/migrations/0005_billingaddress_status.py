# Generated by Django 4.0.1 on 2022-01-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_billingaddress_customer_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='status',
            field=models.CharField(choices=[(0, 'Optional Address'), (1, 'Current_Delivery')], default=0, max_length=100),
        ),
    ]
