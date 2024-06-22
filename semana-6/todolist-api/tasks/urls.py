from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TaskViewSet

# intanciar defaultRouter
router = DefaultRouter()

# registrar rutas
router.register(r"categories", CategoryViewSet)
router.register(r"tasks", TaskViewSet)

urlpatterns = router.urls
