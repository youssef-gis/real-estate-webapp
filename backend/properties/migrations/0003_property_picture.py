# Generated by Django 4.2.1 on 2023-05-26 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_property_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
