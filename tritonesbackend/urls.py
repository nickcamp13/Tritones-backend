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
from django.urls import path, include, re_path
from tritones.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'trackData/', get_track_data),
    path('home/', view_home, name='view_home'),
    path('about-us/', view_about_us, name='view_about_us'),
    path('auditions/', view_auditions, name='view_auditions'),
    path('photos/', view_photos, name='view_photos'),
    path('bookings/', view_bookings, name='view_bookings'),
    path('contact-us/', view_contact_us, name='view_contact_us'),
]
