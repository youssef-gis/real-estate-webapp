from .serializers import PropertySerializer
from properties.models import Property
from rest_framework import generics

class PropertyList(generics.ListAPIView):
    queryset = Property.objects.all().order_by('-date_posted')
    serializer_class = PropertySerializer
    
class PropertyCreate(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetail(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDestroy(generics.DestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyUpdate(generics.UpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer