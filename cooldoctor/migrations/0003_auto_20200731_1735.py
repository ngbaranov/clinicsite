# Generated by Django 3.0.8 on 2020-07-31 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooldoctor', '0002_auto_20200731_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='work_hours',
            field=models.CharField(max_length=250, verbose_name='Часы работы'),
        ),
    ]
