# Generated by Django 3.0.2 on 2020-02-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_plantstest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plants',
            name='user',
            field=models.IntegerField(),
        ),
    ]