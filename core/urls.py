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
from django.conf.urls.i18n import i18n_patterns, set_language


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('i18n/set_language/', set_language, name='set_language'),
    path('fanlar/', fanlar_view, name="fanlar"),
    path("fanlar/<int:pk>/details/", fanlar_details_view),
    path('fanlar/fan_qoshish/', fan_qoshish_view, name="fan_qoshish"),
    path("fanlar/<int:pk>/o'chirish/tasdiqlash/", fan_delete_tasdiqlash_view),
    path("fanlar/<int:pk>/o'chirish/", fan_delete_view),
    path("fanlar/<int:pk>/tahrirlash/", fan_update_view),
    path('yonalishlar/', yonalishlar_view, name="yonalishlar"),
    path('yonalishlar/<int:pk>/details/', yonalish_details_view),
    path('yonalishlar/<int:pk>/update/', yonalish_update_view),
    path('yonalishlar/<int:pk>/delete/tasdiqlash/', yonalish_delete_tasdiqlash_view),
    path('yonalishlar/<int:pk>/delete/', yonalish_delete_view),
    path('yonalishlar/yonalish_qoshish/', yonalish_qoshish_view, name="yonalish_qoshish"),
    path('ustozlar/', ustozlar_view, name="ustozlar"),
    path('ustozlar/<int:pk>/update/', ustoz_update_view),
    path('ustozlar/ustoz_qoshish/', ustoz_qoshish_view, name="ustoz_qoshish"),
    path('ustozlar/<int:ustoz_id>', ustozlar_details_view, name="ustozlar_details"),
    path("ustozlar/<int:pk>/delete/tasdiqlash/", ustoz_delete_tasdiqlash_view),
    path("ustozlar/<int:pk>/delete/", ustoz_delete_view),
]
