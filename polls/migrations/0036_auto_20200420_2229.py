# Generated by Django 3.0.2 on 2020-04-20 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0035_plantdata_vpd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantdata',
            name='NDVI_grade',
            field=models.IntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None, null=True),
        ),
    ]
