
from .views import ProductViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

#  Crear instancia de DefaultRouter
router = DefaultRouter()
# agregar una ruta usando router
router.register(r'products', ProductViewSet) #r para que no haya problemas con el string, ya que existen caracteres especiales y los caracteres extra;os los coloca como texto
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls
# path('products/', get_products, name='products_list')


