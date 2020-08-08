# Generated by Django 3.0.8 on 2020-08-06 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooldoctor', '0007_auto_20200802_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='avatar',
        ),
        migrations.AddField(
            model_name='topmenu',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Аватарка'),
        ),
    ]
