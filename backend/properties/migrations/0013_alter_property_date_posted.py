# Generated by Django 4.2.1 on 2023-05-31 00:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0012_alter_property_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='date_posted',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
