# Generated by Django 4.2.1 on 2023-06-09 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0017_alter_property_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
