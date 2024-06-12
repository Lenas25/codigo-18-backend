# patrones url con los controladores
from django.urls import path
from .views import CategoriaApiView, UnaCategoriaApiView, RegistroUsuarioApiView, PerfilUsuarioApiView
from rest_framework_simplejwt.views import TokenObtainPairView

# registrarlo en el archivo de urls principal con metodo include
urlpatterns = [
    path('categoria', CategoriaApiView.as_view()),
    path('categoria/<int:id>', UnaCategoriaApiView.as_view()),
    path('registro', RegistroUsuarioApiView.as_view()),
    path('login', TokenObtainPairView.as_view()), #vista del propio rest_framework jwt, te da tu propio token
    path('perfil', PerfilUsuarioApiView.as_view()),
]
