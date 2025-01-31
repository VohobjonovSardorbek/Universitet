from tkinter.font import names

from django.contrib import admin
from django.urls import path

from mainApp.views import *

"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('fanlar/', fanlar_view, name="fanlar"),
    path('fanlar/fan_qoshish/', fan_qoshish_view, name="fan_qoshish"),
    path('yonalishlar/', yonalishlar_view, name="yonalishlar"),
    path('yonalishlar/yonalish_qoshish/', yonalish_qoshish_view, name="yonalish_qoshish"),
    path('ustozlar/', ustozlar_view, name="ustozlar"),
    path('ustozlar/ustoz_qoshish/', ustoz_qoshish_view, name="ustoz_qoshish"),
    path('ustozlar/<int:ustoz_id>', ustozlar_details_view, name="ustozlar_details"),
]
