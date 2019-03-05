from django import forms

from .models import Marca, Modelo

class MarcaForm(forms.ModelForm):
    marca_clave = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Clave','aria-describedby':'Agregar Clave'}))
    marca_nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre','aria-describedby':'Agregar Nombre'}))
    marca_descripcion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripción','aria-describedby':'Agregar Descripción'}))
    class Meta:
        model = Marca
        fields = ['marca_clave','marca_nombre','marca_descripcion',]
    
class ModeloForm(forms.ModelForm):
    modelo_clave = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Clave','aria-describedby':'Agregar Clave'}))
    modelo_nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre','aria-describedby':'Agregar Nombre'}))
    modelo_descripcion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripción','aria-describedby':'Agregar Descripción'}))
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Modelo
        fields = ['modelo_clave','modelo_nombre','modelo_descripcion','marca',]
