from .views import ProductView
from django.urls import path

urlpatterns = [
    path('product/', ProductView.as_view(), name='product'), # -> el name sirve para referenciar la url y por ejemplo utilizar en redirecciones
]
