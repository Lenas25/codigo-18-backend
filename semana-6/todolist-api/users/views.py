from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .models import User
from .serializers import UserSerializer, UserLoginSerializer
from .utils import get_tokens_for_user

# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Aqui se especifican los metodos


class AuthenticationView(APIView):
    def post(self, request):
        # request.data es la informacion que se recibe del cliente
        user_request = UserLoginSerializer(data=request.data)
        if not user_request.is_valid():
            return Response(
                data={
                    "message": user_request.errors
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        # buscar al usuario por correo, user -> objeto tipo base de datos o Django ORM
        user = User.objects.get(email=user_request.data['email'])
        if not user:
            return Response(
                data={
                    "message": user_request.errors
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        # comparar que el password sea correcto, user_serializer -> parsear de la base de datos a json
        user_serializer = UserSerializer(user).data
        if not check_password(user_request.data['password'], user_serializer['password']):
            return Response(
                data={
                    "message": "Email or password incorrect"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        token = get_tokens_for_user(user);
        
        return Response(
            data={
                "user": user_serializer,
                "access_token": token['access'],
                'refresh_token': token['refresh']
            },
            status=status.HTTP_200_OK
        )
