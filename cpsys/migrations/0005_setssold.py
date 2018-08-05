# Generated by Django 2.0.7 on 2018-08-04 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpsys', '0004_auto_20180804_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetsSold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_sold', models.CharField(max_length=20, verbose_name='Set')),
                ('date_sold', models.DateTimeField(auto_now=True)),
                ('sold_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpsys.Member')),
            ],
        ),
    ]