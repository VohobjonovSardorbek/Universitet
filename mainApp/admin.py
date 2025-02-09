from django.contrib import admin

from .models import *


class FanAdmin(admin.ModelAdmin):
    list_display = ['nom']
    list_display_links = ['nom']
    list_filter = ['asosiy', 'yonalish']
    search_fields = ['nom']


class FanInline(admin.StackedInline):
    model = Fan
    extra = 1


class UstozAdmin(admin.ModelAdmin):
    list_display = ['ism', 'daraja', 'fan']
    list_display_links = ['ism', 'fan']
    search_fields = ['ism']
    list_filter = ['daraja']


class YonalishAdmin(admin.ModelAdmin):
    list_display = ['nom', 'aktiv']
    list_display_links = ['nom']
    list_editable = ['aktiv']
    list_filter = ['aktiv']
    search_fields = ['nom']
    inlines = [FanInline]

admin.site.register(Ustoz, UstozAdmin)
admin.site.register(Yonalish, YonalishAdmin)
admin.site.register(Fan, FanAdmin)