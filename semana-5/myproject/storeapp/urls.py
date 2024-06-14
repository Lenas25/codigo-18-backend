
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter

#  Crear instancia de DefaultRouter
router = DefaultRouter()
# agregar una ruta usando router
router.register(r'products', ProductViewSet) #r para que no haya problemas con el string

urlpatterns = router.urls
# path('products/', get_products, name='products_list')


