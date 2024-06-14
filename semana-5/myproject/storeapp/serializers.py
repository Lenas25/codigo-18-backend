from rest_framework.serializers import ModelSerializer
from .models import Product

# Luego de importar ambas clases podemos crear nuestra clase serializer
class ProductSerializer(ModelSerializer):
  class Meta:
    # definir el modelo que usara el serializer
    model = Product
    # definir cuales son los campos que quiero usar del modelo
    fields = '__all__'