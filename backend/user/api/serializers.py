from rest_framework import serializers
from properties.api.serializers import PropertySerializer
from user.models import Profile
from properties.models import Property

class ProfileSerializer(serializers.ModelSerializer):
    seller_properties = serializers.SerializerMethodField()

    def get_seller_properties(self, obj):
        properties = Property.objects.filter(seller=obj.seller)
        return PropertySerializer(properties, many=True).data
    class Meta:
        model = Profile
        fields = '__all__'
    
