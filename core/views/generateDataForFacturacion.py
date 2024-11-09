from rest_framework.response import Response # type: ignore
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from SistemaRV.decorators import jwt_required
from SistemaRV.decorators import CustomJWTAuthentication
from rest_framework.views import APIView
from rest_framework import status
import requests
from core.models import Entidad, Comprobante, ComprobanteItem

class GenerateFacturacionFromIds(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    
    
    @swagger_auto_schema(
        operation_summary="Generate Facturación",
        operation_description="Generate a facturación document based on specified IDs and other details.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['comprobante', 'emisor', 'comprador', 'items', 'payTerms', 'observaciones', 'tipoPago'],
            properties={
                'comprobante': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the comprobante"),
                'emisor': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the emisor"),
                'comprador': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the comprador"),
                'items': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the item"),
                            'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description="Quantity of the item")
                        }
                    ),
                    description="List of items with id and quantity"
                ),
                'payTerms': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'metodo': openapi.Schema(type=openapi.TYPE_STRING, description="Payment method")
                        }
                    ),
                    description="List of payment terms, each with a metodo"
                ),
                'observaciones': openapi.Schema(type=openapi.TYPE_STRING, description="Observations for the document"),
                'tipoPago': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the payment type"),
            },
            description="Data required to generate a facturación document"
        ),
        responses={
            200: openapi.Response(description="Successful Request", examples={"application/json": {"response": "Successful Request"}}),
            400: openapi.Response(description="Bad Request")
        }
    )
    @jwt_required
    def post(self, request, *args):
        data = request.data
        
        # Required keys for validation
        required_keys = {
            'comprobante': int,
            'emisor': int,
            'comprador': int,
            'items': list,
            'payTerms': list,
            'observaciones': str,
            'tipoPago': int,
        }
        
        # Check if each required key is in the data
        for key, expected_type in required_keys.items():
            if key not in data:
                return Response({"error": f"'{key}' is a required field."}, status=status.HTTP_400_BAD_REQUEST)
            if not isinstance(data[key], expected_type):
                return Response({"error": f"'{key}' must be of type {expected_type.__name__}."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check that items is a list of dictionaries with 'id' and 'quantity' keys
        for item in data['items']:
            if not isinstance(item, dict) or 'id' not in item or 'quantity' not in item:
                return Response({
                    "error": "Each item in 'items' must be a dictionary with 'id' and 'quantity' keys."
                }, status=status.HTTP_400_BAD_REQUEST)
        
        # Check that payTerms is a list of dictionaries with 'metodo' key
        for term in data['payTerms']:
            if not isinstance(term, dict) or 'metodo' not in term:
                return Response({
                    "error": "Each entry in 'payTerms' must be a dictionary with a 'metodo' key."
                }, status=status.HTTP_400_BAD_REQUEST)
                
        sendData = {
            "comprobante" : {},
            "taxes" : {},
            "items" : [],
            "payterms" : data["payTerms"],
            "observaciones" : data["observaciones"],
            "formaPago" : data["formaPago"],
            "tipo_pdf" : data['tipo_pdf'],
        }
        
        emisor = Entidad.objects.filter(id=data["emisor"]).first()
        
        sendData["emisor"] = {
            "TipoDocumento": emisor.tipoDocumento.codigo,
                "DocumentoEmisor": emisor.numeroDocumento,
                "RazonSocialEmisor": emisor.razonSocial,
                "ubigeo": emisor.ubigeo.codigo,
                "calle": emisor.direccion,
                "distrito": emisor.ubigeo.distrito,
                "provincia": emisor.ubigeo.provincia,
                "departamento": emisor.ubigeo.departamento,
                "email" : '',
                'telefono' : emisor.celular,
        }
        
        adquiriente = Entidad.objects.filter(id=data["adquiriente"]).first()
        
        sendData["adquiriente"] = {
                "TipoDocumentoAdquiriente": adquiriente.tipoDocumento.codigo,
                "NumeroDocumentoAdquiriente": adquiriente.numeroDocumento,
                "razonSocial": adquiriente.razonSocial,
                "CalleComprador": adquiriente.direccion,
                "distritoComprador": adquiriente.ubigeo.distrito,
                "provinciaComprador": adquiriente.ubigeo.provincia,
                "departamentoComprador": adquiriente.ubigeo.departamento
            }
        
        try:
            item_ids = [item['id'] for item in data['items']]
            item_detail_url = "http://54.235.246.131:8002//api/custom-item-view/"
            items = []
            response = requests.get(item_detail_url, params={"ids": ",".join(map(str, item_ids)), "resupuesta_simple": "false"})
            if response.status_code == 200:
                items = response.json()  # Assuming the response JSON is already a list of items
            else:
            # Handle any errors, such as logging or raising an exception
                return Response(f"Error fetching items: {response.status_code}")
            if response.status_code != 200:
                return Response({"error": "Failed to retrieve item details from custom-item-view."}, status=response.status_code)
            item_details = []
            # Add fetched item details to response data
            numeroId=1
            for item in items['results']:
                for value in data['items']:
                    if value['id'] == item['id']:
                        cantidad = value['quantity']
                        
                dataToAdd = {
                    "unidadMedida": item["unidadMedida"]["codigo"],
                    "CantidadUnidadesItem": cantidad,
                    "totalValorVenta": item["valorUnitario"] * cantidad,
                    "precioUnitarioConImpuestos": item["valorUnitario"],
                    "tipoPrecio": item["tipoPrecio"]["codigo"],
                    "totalTax": 30.51,
                    "DescripcionItem": item["descripcion"],
                    "id": f"PROD{numeroId}",
                    "precioUnitario":84.75,
                    'codProducto' : item["codigoProducto"]["codigo"],
                    'descripcion': item["descripcion"],
                    'tax' : {},
                }
                numeroId +=1
                totaltax = 0
                totalPercentage = 0
                for tax in item['taxes']:
                    totalPercentage += tax['porcentaje']
                totalPercentage = totalPercentage/100
                
                dataToAdd['precioUnitario'] = item['valorUnitario'] * (1-totalPercentage)
                
                for tax in item['taxes']:
                    dataToAdd['tax'][tax['impuesto']['nombre']] = {
                            "operacionesGravadas": (item['valorUnitario'] * cantidad)*(1-totalPercentage),
                            "MontoTotalImpuesto": (item['valorUnitario'] * cantidad)*(1-totalPercentage)*(tax['porcentaje']/100),
                            "cod1": tax['impuesto']["codigo"],
                            "cod2": tax['impuesto']["nombre"],
                            "cod3": tax['impuesto']["un_ece_5153"],
                            "afectacionIGV": tax['afectacion'],
                    }
                    totaltax += (item['valorUnitario'] * cantidad)*(1-totalPercentage)*(tax['porcentaje']/100)
                dataToAdd['totalTax'] = totaltax
                item_details.append(item)
                
                sendData['items'].append(dataToAdd)
            data['item_details'] = item_details

        except requests.RequestException as e:
            return Response({"error": f"Internal API call failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        # If all checks pass, return a success response
        return Response({'response': sendData})
    
if __name__ == '__main__':
    data = {
        'comprobante': 1,
        'emisor' : 1,
        'comprador' : 2,
        'items' : [
            {'id': 6,
            'quantity' : 5},
            {'id': 9,
            'quantity' : 1}
        ],
        "payTerms": [
            {
                "metodo": "contado",
            }
        ],
        'observaciones': 'Observaciones para poner en el documento pdf',
        'tipoPago': 3,
    }