from .models import *
from contextlib import contextmanager
from idlelib.query import Query

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def home_view(request):
    return render(request, 'index.html')

def fanlar_view(request):
    fanlar = Fan.objects.all()

    context = {
        "fanlar" : fanlar,
    }
    return render(request, 'fanlar.html', context=context)

def fan_qoshish_view(request):
    if request.method == 'POST':
        if request.POST.get('asosiy_id') == '1':
            asosiy = "Asosiy"
        else:
            asosiy = "Qo'shimcha"
        Fan.objects.create(
            nom=request.POST.get('nom'),
            yonalish=Yonalish.objects.get(id=request.POST.get('yonalish_id')),
            asosiy=asosiy,
        )
        return redirect('fanlar')
    yonalishlar = Fan.objects.all()
    asosiylar = Fan.objects.order_by('asosiy').values_list('asosiy', flat=True).distinct()
    context = {
        "yonalishlar" : yonalishlar,
        "asosiylar" : asosiylar,
    }
    return render(request, 'fan_qoshish.html', context=context)

def yonalishlar_view(request):
    yonalishlar = Yonalish.objects.all()
    context = {
        "yonalishlar" : yonalishlar,
    }
    return render(request, 'yonalishlar.html', context=context)

def yonalish_qoshish_view(request):
    if request.method == 'POST':
        Yonalish.objects.create(
            nom=request.POST.get('nom'),
            aktiv=request.POST.get('aktiv') == 'on'
        )
        return redirect('yonalishlar')
    return render(request, 'yonalish_qoshish.html')

def ustozlar_view(request):
    ustozlar = Ustoz.objects.all()
    context = {
        "ustozlar" : ustozlar
    }
    return render(request, 'ustozlar.html', context=context)

def ustoz_qoshish_view(request):
    if request.method == 'POST':
        if request.POST.get('jins') == '1':
            jins="Erkak"
        else:
            jins="Ayol"
        if request.POST.get('daraja_id') == "1":
            daraja="Bakalavr"
        elif request.POST.get('daraja_id') == "2":
            daraja="Magistr"
        else:
            daraja="Doktorant"

        Ustoz.objects.create(
            ism=request.POST.get('ism'),
            yosh=request.POST.get('yosh'),
            jins=jins,
            daraja=daraja,
            fan=Fan.objects.get(id=request.POST.get('fan_id'))
        )
        return redirect('fanlar')

    fanlar = Fan.objects.all()
    context = {
        "fanlar" : fanlar
    }
    return render(request, 'ustoz_qoshish.html', context=context)

def ustozlar_details_view(request, ustoz_id):
    ustoz = Ustoz.objects.get(id=ustoz_id)

    context = {
        "ustoz" : ustoz
    }
    return render(request, 'ustozlar_details.html', context=context)