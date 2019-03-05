from django.contrib import admin

# Register your models here.

from .models import Marca, Modelo

admin.site.register(Marca)
admin.site.register(Modelo)