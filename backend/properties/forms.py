from typing import Any, Dict, Mapping, Optional, Type, Union

from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Poi
from django import forms
from django.contrib.gis.geos import Point

class PoiForm(forms.ModelForm):
    class Meta : 
        model = Poi
        fields = [
            'name','description','type','location',
            'latitude', 'longitude']
    latitude = forms.FloatField()
    longitude = forms.FloatField()

    def clean(self) -> Dict[str, Any]:
        data= super().clean()
        latitude = data.pop('latitude')
        longitude = data.pop('longitude')
        data['location'] = Point(latitude, longitude, srid=4326)
        return data

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        location = self.initial.get('location')
        if isinstance(location, Point):
            self.initial['latitude'] = location.tuple[0]
            self.initial['longitude'] = location.tuple[1]
