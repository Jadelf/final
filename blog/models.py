from django.db import models
from django.utils import timezone
from django.contrib import admin

class Plato(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre

class Menu(models.Model):
    nombre=models.CharField(max_length=80)
    precio=models.CharField(max_length=10)
    empleado=models.CharField(max_length=80)
    cliente=models.CharField(max_length=80)
    register_date=models.DateTimeField(default=timezone.now)
    platos=models.ManyToManyField(Plato,through='Asignacion')
    def __str__(self):
        return self.nombre

class Asignacion(models.Model):
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato,on_delete=models.CASCADE)

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class PlatoAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class MenuAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)
