# Generated by Django 2.0.7 on 2018-08-05 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpsys', '0011_auto_20180805_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamrecord',
            name='date_added',
        ),
        migrations.AddField(
            model_name='member',
            name='date_added',
            field=models.DateTimeField(auto_now=True, help_text="When Was Member's Record Added?"),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]