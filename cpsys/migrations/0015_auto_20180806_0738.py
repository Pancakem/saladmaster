# Generated by Django 2.0.7 on 2018-08-06 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpsys', '0014_auto_20180805_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamrecord',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpsys.Member', verbose_name='Member Name'),
        ),
    ]
