# Generated by Django 3.0.2 on 2020-04-21 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0019_auto_20200420_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantprediction',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 21, 21, 25, 34, 328242)),
        ),
    ]