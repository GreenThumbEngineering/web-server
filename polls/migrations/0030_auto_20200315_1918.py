# Generated by Django 3.0.2 on 2020-03-15 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0029_auto_20200315_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantdata',
            name='Nir_pic',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='plantdata',
            name='White_pic',
            field=models.ImageField(upload_to='images'),
        ),
    ]
