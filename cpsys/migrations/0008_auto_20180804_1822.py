# Generated by Django 2.0.7 on 2018-08-04 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpsys', '0007_auto_20180804_1819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='setsold',
            options={'ordering': ['set_sold', 'set_sold_by', 'date_sold'], 'verbose_name_plural': 'Sets Sold'},
        ),
        migrations.RenameField(
            model_name='setsold',
            old_name='sold_by',
            new_name='set_sold_by',
        ),
    ]
