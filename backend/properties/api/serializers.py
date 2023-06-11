from rest_framework import serializers
from properties.models import Property, Poi
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point

class PropertySerializer(serializers.ModelSerializer):
    seller_username = serializers.SerializerMethodField()
    seller_agency_name = serializers.SerializerMethodField()
    propertyPoi = serializers.SerializerMethodField()
    
    def get_seller_username(self, obj):
        return obj.seller.username
    def get_seller_agency_name(self, obj):
        return obj.seller.profile.agency_name
    
    def get_propertyPoi(self, obj):
        property_locations = Point(obj.latitude, obj.longitude, srid=4326)
        query = Poi.objects.filter(location__distance_lte=(property_locations, D(km=10)))
        querySerialized = PoiSerializer(query, many=True)
        return querySerialized.data

    class Meta:
        model = Property
        fields = '__all__'
    
    
class PoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poi
        fields = '__all__'