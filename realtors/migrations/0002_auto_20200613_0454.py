# Generated by Django 3.0.7 on 2020-06-13 04:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 6, 13, 4, 54, 6, 777050)),
        ),
    ]
