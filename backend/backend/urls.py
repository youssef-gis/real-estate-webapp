"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import properties.api.views as property_api_view
import user.api.views as user_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/list_properties/', property_api_view.PropertyList.as_view()),
    path('api/list_properties/create/', property_api_view.PropertyCreate.as_view()),
    path('api/list_properties/<int:pk>/', property_api_view.PropertyDetail.as_view()),
    path('api/list_properties/<int:pk>/update/', property_api_view.PropertyUpdate.as_view()),
    path('api/list_properties/<int:pk>/delete/', property_api_view.PropertyDestroy.as_view()),
    path('api/profiles/', user_api_view.ProfileList.as_view()),
    path('api/profiles/<int:seller>/', user_api_view.ProfileDetail.as_view()),
    path('api/profiles/<int:seller>/update/', user_api_view.ProfileUpdate.as_view()),
    path("api-auth-djoser/", include('djoser.urls')),
    path("api-auth-djoser/", include('djoser.urls.authtoken'))     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
