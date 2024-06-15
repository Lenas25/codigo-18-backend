from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.viewsets import ModelViewSet # La clase de rest framework que te permite crear un crud

# El ModelViewSet permite que se puedan hacer todas las operaciones CRUD, ademas con el queryset y serializer class se activa la funcionalidad de la clase
# el permission classes es para definir que tipo de permisos se necesitan para acceder a la vista
# para hacer put y delete se necesita el id del producto
class ProductViewSet(ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = []

class CategoryViewSet(ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = []









