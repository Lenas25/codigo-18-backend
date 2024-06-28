
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    # esta ruta es para autenticar -> pide el email y password en base a eso se crea un token
    # usa la tabla auth_user de django
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # usa la ruta para otro tiempo de vida al token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('payments.urls'))
]
