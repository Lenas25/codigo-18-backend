from django.db import models

# Create your models here.


class CategoriaModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=100, unique=True, null=False)
    # Campos de auditoria, creados automaticamente por la base de datos, solo para visualizacion
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    # Se modificara el valor cada vez que hagamos una modificacion a las otras columnas con la fecha hora actual
    updatedAt = models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        db_table = 'categorias'

class ProductoModel(models.Model):
  id = models.AutoField(primary_key=True, unique=True, null=False)
  nombre = models.CharField(max_length=100, null=False)
  precio = models.FloatField(null=False)
  disponible = models.BooleanField(default=True)
  createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
  
  # relaciones de uno a muchos on delete hay en CASCADE, PROTECT y DO_NOTHING
  categoria = models.ForeignKey(to=CategoriaModel, on_delete=models.CASCADE, db_column='categoria_id')
  
  class Meta:
    db_table = 'productos'