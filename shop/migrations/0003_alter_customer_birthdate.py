# Generated by Django 4.0.1 on 2022-01-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_user_id_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birthdate',
            field=models.DateTimeField(),
        ),
    ]