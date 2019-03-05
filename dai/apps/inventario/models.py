from django.db import models

# Create your models here.

class Marca(models.Model):
    marca_clave = models.CharField(max_length=50)
    marca_nombre = models.CharField(max_length=50)
    marca_descripcion = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.marca_nombre

class Modelo(models.Model):
    modelo_clave = models.CharField(max_length=50)
    modelo_nombre = models.CharField(max_length=50)
    modelo_descripcion = models.TextField(max_length=1000)
    marca = models.ForeignKey(Marca, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.modelo_clave
        

'''
class Producto(models.Model):
    producto_tipo = models.CharField(max_length=50)
    producto_unidad_entrada = models.CharField(max_length=50)
    producto_unidad_salida = models.CharField(max_length=100)
    producto_moneda = models.CharField(max_length=100)
    producto_costeo = models.CharField(max_length=100)
    producto_proveedor = models.CharField(max_length=100)
    producto_impuesto = models.CharField(max_length=100)
    producto_marca = models.CharField(max_length=100)
    producto_modelo = models.CharField(max_length=100)
    producto_clave = models.CharField(max_length=100)
    producto_color = models.CharField(max_length=100)
    producto_clave_alterna = models.CharField(max_length=100)
    producto_descripcion = models.CharField(max_length=100)
    producto_cuenta_contable = models.CharField(max_length=100)
    producto_sku = models.CharField(max_length=100)
    producto_codigo_barras = models.CharField(max_length=100)
    producto_numero_serie = models.CharField(max_length=100)
    producto_costo = models.CharField(max_length=100)
    producto_precio = models.CharField(max_length=100)
    producto_clave_sat = models.CharField(max_length=100)
    
    def __str__(self):
        return self.marca_clave
'''