# Generated by Django 2.2.7 on 2020-01-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='deviceID',
            field=models.CharField(max_length=25),
        ),
    ]
