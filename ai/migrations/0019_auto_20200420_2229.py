# Generated by Django 3.0.2 on 2020-04-20 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0018_auto_20200403_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantprediction',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 22, 29, 24, 385702)),
        ),
    ]
