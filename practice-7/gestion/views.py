from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import GenerarBoletaSerializer
from datetime import datetime
from .models import *
from os import environ
import requests
import mercadopago
# Create your views here.


class GenerarBoleta(APIView):
  
    def get(self, request:Request, serie, numero):
      data = {
        'operacion': 'consultar_comprobante',
        'tipo_de_comprobante': 2,
        'serie': serie,
        'numero': numero,
      }
      
      peticion = requests.post(url = environ.get('NUBEFACT_URL'), headers = {
        'Authorization': 'Bearer ' + environ.get('NUBEFACT_TOKEN')
      }, json=data)
      
      print(peticion.json())
      resultado = peticion.json()
      
      return Response(
        data = resultado,
        status = peticion.status_code
      )
  
  
    def post(self, request: Request):
        serializador = GenerarBoletaSerializer(data=request.data)
        
        serializador.is_valid(raise_exception=True) # es como un try catch
        
        items = []
        total_general = 0
        total_igv = 0
        body = serializador.validated_data
        print(body)
        for item in body.get('items'):
          producto_encontrado = Producto.objects.filter(id=item['id']).first()
          if not producto_encontrado:
            return Response(
                data={'message': 'Producto no encontrado'},
                status=404
            )
          
          base = producto_encontrado.precio /0.18 # 18% de igv
          
          producto = {
            'unidad_de_medida': 'NIU',
            'codigo': producto_encontrado.id,
            'descripcion': producto_encontrado.nombre,
            'cantidad': item.get('cantidad'),
            'valor_unitario': base,  # no tiene igv
            'precio_unitario': producto_encontrado.precio,  # con igv
            'subtotal': base * item.get('cantidad'),
            'tipo_de_igv': 1,
            'igv': (producto_encontrado.precio - base) * item.get('cantidad'),
            'total': producto_encontrado.precio * item.get('cantidad'),
            'anticipo_regularizacion': False,
          }
        
          total_general += producto_encontrado.precio * item.get('cantidad')
          total_igv += (producto_encontrado.precio - base) * item.get('cantidad')
          items.append(producto)
          
        data = {
            'operacion': 'generar_comprobante',
            'tipo_de_comprobante': 2,
            'serie': 'BBB1',
            'numero': 1,
            'sunat_transaction': 1,
            'cliente_tipo_de_documento': 1,
            'cliente_numero_de_documento': body.get('documento_usuario'),
            'cliente_denominacion': body.get('nombre_usuario'),
            'fecha_de_emision': datetime.now().strftime('%d-%m-%Y'),
            'moneda': 1,
            'total_igv': total_igv,
            'total_gravada': total_general - total_igv,
            'porcentaje_de_igv': 18.0,
            'total': total_general,
            'items': items
        }
        
        # para enviar la data a la nubefact
        peticion = requests.post(url = environ.get('NUBEFACT_URL'), headers = {
          'Authorization': 'Bearer ' + environ.get('NUBEFACT_TOKEN')
        }, json = data)
        
        print(peticion.json())
        print(peticion.status_code)

        return Response(
            data={
                'data': data,
                'message': 'Boleta generada correctamente'
            },
            status=200
        )

class GenerarPago(APIView):
  def post(self, request:Request):
    # inicializar sdk
    sdk = mercadopago.SDK(environ.get('MERCADOPAGO_TOKEN'))
    # crear preferencia
    respuesta = sdk.preference().create({
      "items":[
        {
          "id":1,
          "title":"Audifonos",
          "description":"Audifonos inalambricos marca x",
          "quantity":1,
          # "currency_id":"PEN",
          "unit_price":89.5
        }
      ],
      # para saber si se realizo el pago o el estado del pago, se debe agregar un link publico para que mercadopago pueda notificar, en este caso se usa ngrok (es un ejemplo )
      "notification_url":"http://webhook.site/3b1f4b7d-3b1f-4b7d-8b7d-3b1f4b7d3b1f",
    })
    
    print(respuesta)
    return Response({
      'content': respuesta,
    })
  
# este decorador permite que haya una vista que reciba peticiones de tipo get y post
@api_view(http_method_names=['GET','POST'])
def webhooks_mp(request:Request):
  print(request.data)
  print(request.query_params)
  
  return Response({
    'message': 'Webhook recibido'
  }, status=200)