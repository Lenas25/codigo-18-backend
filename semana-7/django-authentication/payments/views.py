import mercadopago
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PaymentsWithMercadoPagoView(APIView):
  def post(self, request):
    # inicializar mercado pago con el access token privado
    mercadopage_sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)
    
    preference_data = {
      "items": [
        # recibe un arreglo de productos y enviar eso en marcado pago para el detalle de las ventas
        {
          "title": request.data.get("title"),
          "quantity": int(request.data.get('quantity')),
          "currency_id":"PEN",
          "unit_price":float(request.data.get("unit_price")),
        }
      ],
      # estas url son a las que nos van a redirigir despues de hacer el pago
      "back_urls":{
        "success": "http://localhost:5173?status=success",
        "failure": "http://localhost:5173?status=failure",
        "pending": "http://localhost:5173?status=pending",
      },
      # para que cuando termine de hacer el pago vuevla inmediatamente a una de las 3 opciones que existen en back url
      "auto_return": "approved"
    }
    
    # es para crear el preference dependiendo de la data recibida y almacenamos en cada variable
    preference_response = mercadopage_sdk.preference().create(preference_data)
    # preference_id = preference_response["id"]
    
    return Response({
      "preference":preference_response
    }, status=status.HTTP_201_CREATED)
