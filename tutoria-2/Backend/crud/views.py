from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ProductoSerializer

# Create your views here.

# obligatorio APIView -> util cuando necesitas control fino sobre logica
# ViewSets -> permite crud sin definidir explicitamente los metosos de cada accion
class ProductView(APIView):
  def post(self, req):
    serializer = ProductoSerializer(data=req.data) # -> revisar si los datos que estamos enviando son validos
    if serializer.is_valid(): # -> retorna un booleano
      serializer.save() # -> para que lo que estemos enviando se guarde en la base de datos
      return Response(data={
        'message': 'Producto creado exitosamente',
        'data': serializer.data
        }, status=status.HTTP_201_CREATED)
      
    # serializer.error_messages
    return Response(data={
        'message': 'Error al crear el producto',
      }, status=status.HTTP_400_BAD_REQUEST)
