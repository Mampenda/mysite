# Generated by Django 3.2.4 on 2021-07-14 13:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_item_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
