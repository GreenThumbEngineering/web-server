# Generated by Django 3.0.2 on 2020-03-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_auto_20200315_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantdata',
            name='NDVI_grade',
            field=models.IntegerField(blank=True, choices=[(1, 'Dead'), (2, 'Low'), (3, 'Normal'), (4, 'Good'), (5, 'Excellent')], default=None, null=True),
        ),
    ]
