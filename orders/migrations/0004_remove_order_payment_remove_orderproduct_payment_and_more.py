# Generated by Django 4.0.5 on 2022-07-12 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='payment',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]