# Generated by Django 3.0.7 on 2020-06-13 04:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20200613_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
