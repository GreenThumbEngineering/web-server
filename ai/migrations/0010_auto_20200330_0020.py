# Generated by Django 3.0.2 on 2020-03-29 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0009_auto_20200315_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantprediction',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 30, 0, 20, 2, 817340)),
        ),
    ]
