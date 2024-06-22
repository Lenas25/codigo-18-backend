from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from users.utils import validate_token, get_payload_from_token
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer

# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # hace referencia al endpoint get, solo listar se valida
    def list(self, request):
        header = request.headers.get('Authorization')
        if header is None:
            return Response({
                'message': "Token is required"
            })
        
        token_from_client = header.split()[1]
        if not validate_token(token_from_client):
            return Response({
                'message': "Token no valid"
            })
        payload = get_payload_from_token(token_from_client)
        current_user = UserSerializer(User.objects.get(pk=payload.get('user_id'))).data
        
        if not current_user.get('is_superuser'):
            return Response({
                'message':'You dont have permition to enter'
            })
        
        queryset = TaskSerializer(Task.objects.filter(user_id = current_user.get('id')), many=True).data
        return Response(queryset)
        # -> es para filtrar solo los task con id igual al del usuario de ahora que se logeo
