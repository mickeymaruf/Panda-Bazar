# Generated by Django 4.0.5 on 2022-06-26 08:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/category-images'),
            preserve_default=False,
        ),
    ]
