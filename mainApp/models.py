from django.db import models
from django.db.models import SET_NULL, CharField


class Yonalish(models.Model):
    nom = models.CharField(max_length=255)
    aktiv = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "Yo'nalishlar"


class Fan(models.Model):
    FAN_CHOICES = (
        ("Asosiy", "Asosiy"),
        ("Qo'shimcha", "Qo'shimcha")
    )
    nom = models.CharField(max_length=255)
    yonalish = models.ForeignKey(Yonalish, on_delete=SET_NULL, null=True)
    asosiy = models.CharField(max_length=50, default="Asosiy", choices=FAN_CHOICES)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "Fanlar"


class Ustoz(models.Model):
    JINS_CHOICES = (
        ("Erkak", "Erkak"),
        ("Ayol", "Ayol")
    )
    DARAJA_CHOICES = (
        ("Bakalavr", "Bakalavr"),
        ("Magistr", "Magistr"),
        ("Doktorant", "Doktorant")
    )
    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=20, default="Erkak", choices=JINS_CHOICES)
    yosh = models.PositiveSmallIntegerField(default=25)
    daraja = models.CharField(max_length=30, default="Magistr", choices=DARAJA_CHOICES)
    fan = models.ForeignKey(Fan, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = "Ustozlar"
