from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AuthenticationView
from django.urls import path

router = DefaultRouter()

# router.register solo soporta ViewSets
router.register(r'users', UserViewSet)
# para APIView
urlpatterns = [
    path(r'login', AuthenticationView.as_view()), 
    *router.urls]
