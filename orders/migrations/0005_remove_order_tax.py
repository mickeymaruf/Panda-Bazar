# Generated by Django 4.0.5 on 2022-07-13 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_order_payment_remove_orderproduct_payment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tax',
        ),
    ]