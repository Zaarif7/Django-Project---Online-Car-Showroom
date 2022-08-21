from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name = 'site_urls'),
    path('', include('showroom.urls'), name = 'showroom_urls')
]
