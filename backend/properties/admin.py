from django.contrib import admin
from .models import Property, Poi
from .forms import PoiForm

class PoiAdmin(admin.ModelAdmin):
    form = PoiForm
   
# Register your models here.
admin.site.register(Property)
admin.site.register(Poi, PoiAdmin)