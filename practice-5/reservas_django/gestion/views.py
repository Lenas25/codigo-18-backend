from rest_framework import generics, response, status, request, permissions
from .models import CategoriaModel, UsuarioModel
from .serializers import CategoriaSerializer, RegistroUsuarioSerializer, MostrarUsuarioSerializer
from .permissions import SoloAdministrador

class CategoriaApiView(generics.ListCreateAPIView):
  permission_classes = [permissions.IsAuthenticated,SoloAdministrador]
  # objects -> atributo propio de base de datos, hace un select * from categorias
  queryset = CategoriaModel.objects.all()
  serializer_class = CategoriaSerializer
  

class UnaCategoriaApiView(generics.RetrieveUpdateDestroyAPIView):
  # sobreescribir el metodo get 
  def get(self, request, id):
    # Select * from categorias where id=...
    result = CategoriaModel.objects.filter(id = id).first()
    if result is None:
      return response.Response(
      data={
        'message':'La categoria no existe'
      },
      status=status.HTTP_404_NOT_FOUND
    )
    
    serializado = CategoriaSerializer(instance=result)
    # convierte la instancia a un diccionario -> .data
    return response.Response(
      data={
        'message':'ok',
        'categoria':serializado.data
      },
      status=status.HTTP_200_OK
    )
  # para actualizar la data de db
  def put(self, request: request.Request, id):
    result = CategoriaModel.objects.filter(id = id).first()
    if result is None:
      return response.Response(
      data={
        'message':'La categoria no existe'
      },
      status=status.HTTP_404_NOT_FOUND
    )
    
    # data serializada del request
    data_serializada = CategoriaSerializer(data=request.data)
    
    if data_serializada.is_valid():
      result.nombre = data_serializada.data['nombre']
      result.save()
      return response.Response(
      data={
        'message':'ok',
        'categoria actualizada':data_serializada.data
      },
      status=status.HTTP_200_OK
    )
    else:
      return response.Response(
      data={
        'message':'Error al actualizar la categoria',
        'content': data_serializada.errors
      },
      status=status.HTTP_400_BAD_REQUEST
      )
  
  def delete(self, id):
    result = CategoriaModel.objects.filter(id=id).first()
    if result is None:
      return response.Response(
        data={
          'message':"La categoria no existe"
        },
        status=status.HTTP_404_NOT_FOUND
      )
    
    result.delete()
    return response.Response(
        data={
          'message':"Category delete correctly"
        },
        status=status.HTTP_200_OK
      )

class RegistroUsuarioApiView(generics.CreateAPIView):
  def post(self, request: request.Request):
    serializador = RegistroUsuarioSerializer(data=request.data)
    if serializador.is_valid():
      nuevo_usuario = UsuarioModel(**serializador.validated_data)
      nuevo_usuario.set_password(serializador.validated_data.get('password'))
      
      nuevo_usuario.save()
      
      return response.Response(
        data={
          'message': 'Usuario creado exitosamente',
          'usuario': serializador.validated_data
        },
        status = status.HTTP_200_OK
      )
    else:
      return response.Response(
        data={
          'message':'Error al registrar al usuario',
          'content': serializador.errors
        },
        status=status.HTTP_400_BAD_REQUEST
      )
  

class PerfilUsuarioApiView(generics.RetrieveAPIView):
  # indicar que permisos necesitan los usuarios para acceder a esa vista
  permission_classes = [permissions.IsAuthenticated]
  
  def get(self, request: request.Request):
    usuario_encontrado = MostrarUsuarioSerializer(instance=request.user)
    return response.Response(
      data={
        'content': usuario_encontrado.data
      },
      status=status.HTTP_200_OK
    )
