# Generated by Django 2.0.7 on 2018-08-04 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpsys', '0005_setssold'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SetsSold',
            new_name='SetSold',
        ),
    ]