"""
URL configuration for tritonesbackend project.

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
from django.contrib import admin
from django.urls import include, re_path
from django.urls import path, include
from tritones.views import *

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^memberData/', get_member_data),
    re_path(r'^contactData/', submit_contact_form),
    re_path(r'trackData/', get_track_data),
    re_path(r'^photoData', get_photo_data),
    path('tritones/', include('tritones.urls')),
]

