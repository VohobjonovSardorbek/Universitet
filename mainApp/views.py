from django.db.models import FileField

from .forms import FanModel, YonalishForm, UstozForm
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
        "fanlar": fanlar,
    }
    return render(request, 'fanlar.html', context=context)


def fanlar_details_view(request, pk):
    fan = Fan.objects.get(id=pk)
    context = {
        "fan": fan
    }
    return render(request, 'fanlar_details.html', context=context)


def fan_qoshish_view(request):
    form = FanModel()
    if request.method == 'POST':
        fan_model = FanModel(request.POST)
        if fan_model.is_valid():
            fan_model.save()
        return redirect('fanlar')
    yonalishlar = Fan.objects.all()
    asosiylar = Fan.objects.order_by('asosiy').values_list('asosiy', flat=True).distinct()
    context = {
        "yonalishlar": yonalishlar,
        "asosiylar": asosiylar,
        "form" : form
    }
    return render(request, 'fan_qoshish.html', context=context)


def fan_delete_tasdiqlash_view(request, pk):
    fan = Fan.objects.get(id=pk)
    context = {
        "fan": fan
    }
    return render(request, "fan_o'chirish_tasdiqlash.html", context=context)


def fan_delete_view(request, pk):
    fan = Fan.objects.get(id=pk)
    fan.delete()
    return redirect('/fanlar/')


def fan_update_view(request, pk):
    form = FanModel()
    fan = get_object_or_404(Fan, id=pk)
    if request.method == 'POST':
        fan_model = FanModel(request.POST, instance=fan)
        if fan_model.is_valid():
            fan_model.save()
        return redirect('fanlar')
    else:
        form = FanModel(instance=fan)
    fan = get_object_or_404(Fan, id=pk)
    yonalishlar = Yonalish.objects.exclude(id=fan.yonalish.id)
    if fan.asosiy == "Asosiy":
        asosiy = "Qo'shimcha"
    else:
        asosiy = "Asosiy"
    context = {
        "fan": fan,
        "asosiy": asosiy,
        "yonalishlar ": yonalishlar,
        "form" : form
    }
    return render(request, 'fan_tahrirlash.html', context=context)


def yonalishlar_view(request):
    yonalishlar = Yonalish.objects.all()
    context = {
        "yonalishlar": yonalishlar,
    }
    return render(request, 'yonalishlar.html', context=context)


def yonalish_details_view(request, pk):
    yonalish = Yonalish.objects.get(id=pk)
    print(yonalish.aktiv)
    context = {
        "yonalish": yonalish
    }
    return render(request, 'yonalish_details.html', context=context)


def yonalish_update_view(request, pk):
    form = YonalishForm()
    yonalish = get_object_or_404(Yonalish, id=pk)
    if request.method == 'POST':
        yonalish_model = YonalishForm(request.POST, instance=yonalish)
        if yonalish_model.is_valid():
            yonalish_model.save()
        return redirect('/yonalishlar/')
    else:
        form = YonalishForm(instance=yonalish)
    yonalish = Yonalish.objects.get(id=pk)
    context = {
        "yonalish": yonalish,
        "form" : form
    }
    return render(request, 'yonalish_update.html', context=context)


def yonalish_delete_tasdiqlash_view(request, pk):
    yonalish = get_object_or_404(Yonalish, id=pk)
    context = {
        "yonalish": yonalish
    }
    return render(request, 'yonalish_delete.html', context=context)


def yonalish_delete_view(request, pk):
    yonalish = get_object_or_404(Yonalish, id=pk)
    yonalish.delete()
    return redirect('yonalishlar')


def yonalish_qoshish_view(request):
    form = YonalishForm()
    if request.method == 'POST':
        yonalish_model = YonalishForm(request.POST)
        if yonalish_model.is_valid():
            yonalish_model.save()
        return redirect('yonalishlar')
    context = {"form" : form}
    return render(request, 'yonalish_qoshish.html', context=context)


def ustozlar_view(request):
    ustozlar = Ustoz.objects.all()
    context = {
        "ustozlar": ustozlar
    }
    return render(request, 'ustozlar.html', context=context)


def ustoz_qoshish_view(request):
    form = UstozForm()
    if request.method == 'POST':
        ustoz_model = UstozForm(request.POST)
        if ustoz_model.is_valid():
            ustoz_model.save()
        return redirect('ustozlar')

    fanlar = Fan.objects.all()
    context = {
        "fanlar": fanlar,
        "form" : form
    }
    return render(request, 'ustoz_qoshish.html', context=context)


def ustozlar_details_view(request, ustoz_id):
    ustoz = Ustoz.objects.get(id=ustoz_id)

    context = {
        "ustoz": ustoz
    }
    return render(request, 'ustozlar_details.html', context=context)


def ustoz_update_view(request, pk):
    form = UstozForm()
    ustoz = get_object_or_404(Ustoz, id=pk)
    if request.method == 'POST':
        ustoz_model = UstozForm(request.POST, instance=ustoz)
        if ustoz_model.is_valid():
            ustoz_model.save()
        return redirect('/ustozlar/')
    else:
        form = UstozForm(instance=ustoz)
    ustoz = Ustoz.objects.get(id=pk)
    if ustoz.jins == "Erkak":
        jinsi = "Ayol"
    else:
        jinsi = "Erkak"
    fanlar = Fan.objects.exclude(id=ustoz.fan.id)
    context = {
        "ustoz": ustoz,
        "jinsi": jinsi,
        "fanlar": fanlar,
        "form" : form
    }
    return render(request, 'ustoz_update.html', context=context)


def ustoz_delete_tasdiqlash_view(request, pk):
    ustoz = Ustoz.objects.get(id=pk)
    context = {
        "ustoz": ustoz

    }
    return render(request, 'ustoz_delete.html', context=context)


def ustoz_delete_view(request, pk):
    ustoz = Ustoz.objects.get(id=pk)
    ustoz.delete()
    return redirect('ustozlar')
