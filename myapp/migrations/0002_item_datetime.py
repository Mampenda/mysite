# Generated by Django 3.2.4 on 2021-07-14 13:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 14, 13, 40, 53, 94320, tzinfo=utc)),
        ),
    ]