from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Profile(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True, upload_to="profile_pictures/%Y/%m/%d")
    agency_name = models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'Profile of {self.seller.username}'