# Generated by Django 3.0.7 on 2020-06-21 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0005_auto_20200614_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 6, 21, 8, 34, 35, 230904)),
        ),
    ]
