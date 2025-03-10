# Generated by Django 5.1.5 on 2025-01-17 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('asosiy', models.CharField(choices=[('Asosiy', 'Asosiy'), ("Qo'shimcha", "Qo'shimcha")], default='Asosiy', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Fanlar',
            },
        ),
        migrations.CreateModel(
            name='Yonalish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('aktiv', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': "Yo'nalishlar",
            },
        ),
        migrations.CreateModel(
            name='Ustoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], default='Erkak', max_length=20)),
                ('yosh', models.PositiveSmallIntegerField(default=25)),
                ('daraja', models.CharField(choices=[('Bakalavr', 'Bakalavr'), ('Magistr', 'Magistr'), ('Doktorant', 'Doktorant')], default='Magistr', max_length=30)),
                ('fan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.fan')),
            ],
        ),
        migrations.AddField(
            model_name='fan',
            name='yonalish',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.yonalish'),
        ),
    ]
