# Generated by Django 4.2.8 on 2023-12-26 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_rename_uerid_hotelbooking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelbooking',
            name='user',
        ),
    ]
