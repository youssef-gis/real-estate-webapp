# Generated by Django 4.2.1 on 2023-05-26 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_property_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='picture',
        ),
        migrations.AddField(
            model_name='property',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='property',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='property',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d'),
        ),
    ]
