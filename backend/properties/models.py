from django.contrib.gis.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Property(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    description=models.TextField(null=True, blank=True)
    choice_area = (
        ('Inner London', 'Inner London'),
        ('Outer London', 'Outer London'),
    )
    areas = models.CharField(max_length=20, null=True, blank=True, choices=choice_area)

    borough = models.CharField(max_length=50, null=True, blank=True )

    choice_property = (
        ('House', 'House'),
        ('Appartment', 'Appartment'),
        ('Office', 'Office')
    )

    property_type = models.CharField(max_length=50, null=True, blank=True, choices=choice_property)

    choice_status_property = (
        ('Sale','Sale'),
        ('Rent', 'Rent')
    )
    property_status = models.CharField(max_length=50, null=True, blank=True, choices=choice_status_property)

    price = models.DecimalField(max_digits=10, decimal_places=0)

    choice_rental_frequency = (
        ('Month','Month'),
        ('Week', 'Week'),
        ('Day', 'Day')
    )

    rental_frequency = models.CharField(max_length=20, blank=True,null=True, choices=choice_rental_frequency)

    rooms = models.IntegerField(blank=True, null=True)

    furnished = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=datetime.now)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    picture1 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d")
    picture2 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d")
    picture3 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d")
 

    def __str__(self) -> str:
        return self.name


class Poi(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    # latitude = models.FloatField(null=True, blank=True)
    # longitude = models.FloatField(null=True, blank=True)
    # picture1 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d")
    # picture2 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d")
    # picture3 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d")
    choices_type= (
        ('University', 'University'),
        ('Stadium', 'Stadium'),
        ('Hospital', 'Hospital'),
    )
    type = models.CharField(max_length=50, choices=choices_type)
    location = models.PointField(srid=4326, blank=True, null=True)

    def __str__(self) -> str:
        return self.name