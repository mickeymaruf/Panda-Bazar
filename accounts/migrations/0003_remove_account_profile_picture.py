# Generated by Django 4.0.5 on 2022-07-14 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='profile_picture',
        ),
    ]
