from django.urls import path
from .views import PaymentsWithMercadoPagoView, CustomCreatePayment

urlpatterns = [
    path(r'create-preference/', PaymentsWithMercadoPagoView.as_view(), name="mercadopago-create-preference"),
    path(r'create-payment/', CustomCreatePayment.as_view(), name='mercadopago-create-payment')
]
