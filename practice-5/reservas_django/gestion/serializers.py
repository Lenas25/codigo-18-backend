from rest_framework import serializers
from .models import CategoriaModel, UsuarioModel

class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = CategoriaModel
    # para que los validados sean todos los campos de la tabla
    fields = '__all__'
    # exclude = ['id'] => para que no se serialice el campo id, solo se coloca o fields o exclude

class RegistroUsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = UsuarioModel
    fields = '__all__'

class MostrarUsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = UsuarioModel
    exclude = ['password', 'is_staff', 'user_permissions', 'groups', 'last_login', 'is_superuser']