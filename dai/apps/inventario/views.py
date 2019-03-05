from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import *
from .models import *
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name  = 'inventario/index.html'

class HomeIndex(TemplateView):
    template_name  = 'inventario/index.html'

class MarcaIndex(ListView):
    model = Marca
    template_name  = 'inventario/marca/index.html'

class MarcaAdd(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name  = 'inventario/marca/marca_add.html'
    success_url = reverse_lazy('marca')   
            
class MarcaUpdate(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name  = 'inventario/marca/marca_update.html'
    success_url = reverse_lazy('marca')  

class MarcaDelete(DeleteView):
    model = Marca
    form_class = MarcaForm
    template_name  = 'inventario/marca/marca_delete.html'
    success_url = reverse_lazy('marca')

class ModeloIndex(ListView):
    model = Modelo
    template_name  = 'inventario/modelo/modelo_index.html'

class ModeloAdd(CreateView):
    model = Modelo
    form_class = ModeloForm
    template_name  = 'inventario/modelo/modelo_add.html'
    success_url = reverse_lazy('modelo') 

class ModeloUpdate(UpdateView):
    model = Modelo
    form_class = ModeloForm
    template_name  = 'inventario/modelo/modelo_update.html'
    success_url = reverse_lazy('modelo')  

class ModeloDelete(DeleteView):
    model = Modelo
    form_class = ModeloForm
    template_name  = 'inventario/modelo/modelo_delete.html'
    success_url = reverse_lazy('modelo')