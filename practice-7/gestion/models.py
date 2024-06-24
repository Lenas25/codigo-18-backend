from django.db import models

# Create your models here.
class Cabecera(models.Model):
  id = models.AutoField(primary_key=True, null=False)
  fecha = models.DateField(null=False)
  total = models.FloatField(null=False)
  dni = models.CharField(max_length=8, null=False)
  nombre = models.CharField(max_length=100, null=False)
  apellido = models.CharField(max_length=100, null=False)
  
  class Meta:
    db_table = 'cabeceras'

class Producto(models.Model):
  id = models.AutoField(primary_key=True, null=False)
  nombre = models.TextField(null=False)
  precio = models.FloatField(null=False)
  
  class Meta:
    db_table = 'productos'

class Detalle(models.Model):
  cantidad = models.IntegerField(null=False)
  subtotal = models.FloatField(null=False, db_column='sub_total')
  producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='producto_id')
  cabecera = models.ForeignKey(Cabecera, on_delete=models.CASCADE, db_column='cabecera_id')
  
  class Meta:
    db_table = 'detalles'
  