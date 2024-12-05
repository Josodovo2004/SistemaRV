from rest_framework.response import Response # type: ignore
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from SistemaRV.decorators import jwt_required
from SistemaRV.decorators import CustomJWTAuthentication
from rest_framework.views import APIView
from rest_framework import status
import requests
from core.models import Entidad, Comprobante, ComprobanteItem, TipoPago, NotaCredito
from datetime import timedelta
from core.serializers import comprobanteItemSerializer

class GenerateFacturacionFromIds(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    
    
    @jwt_required
    def post(self, request, *args):
        
        data = request.data
        
        #validacion de los datos del request
        
        if type(data['notaCredito']) != int:
            return Response('notaCredito debe ser un entero', status=status.HTTP_400_BAD_REQUEST)
        if type(data['ruc']) != int:
            return Response('ruc debe ser un entero', status=status.HTTP_400_BAD_REQUEST)
        if type(data['observaciones']) != str:
            return Response('observaciones debe ser un string', status=status.HTTP_400_BAD_REQUEST)
        
        
        #validacion de que la nota de credito existe
        
        notaCredito = NotaCredito.objects.filter(id=data['notaCredito'], ).first()
        
        if notaCredito == None:
            return Response(f'No existe una nota de credito con id{notaCredito.id}', status=status.HTTP_400_BAD_REQUEST)
        
        #validacion de que la nota de credito le petenezca al usuario que hizo la peticion
        
        if notaCredito.comprobante.emisor.numeroDocumento != data['ruc']:
            return Response(f'La nota de credito con id {notaCredito.id} no le pertenece a este usuario con ruc {data['ruc']}', status=status.HTTP_400_BAD_REQUEST)
        
        sendData = {
            "comprobante" : {
                "serieDocumento": notaCredito.serie,
                "numeroDocumento": notaCredito.numeroComprobante,
                "fechaEmision": notaCredito.fechaEmision,
                "MontoTotalImpuestos": 0,
                "ImporteTotalVenta": 0,
                "totalConImpuestos": 0
                },
            "emisor": {
                "TipoDocumento": notaCredito.comprobante.emisor.tipoDocumento.codigo,  # RUC
                "DocumentoEmisor": notaCredito.comprobante.emisor.numeroDocumento,
                "RazonSocialEmisor": notaCredito.comprobante.emisor.razonSocial,
                "ubigeo": notaCredito.comprobante.emisor.ubigeo.codigo,
                "calle": notaCredito.comprobante.emisor.direccion,
                "distrito": notaCredito.comprobante.emisor.ubigeo.distrito,
                "provincia": notaCredito.comprobante.emisor.ubigeo.provincia,
                "departamento": notaCredito.comprobante.emisor.ubigeo.departamento
                },
            "adquiriente": {
                 "TipoDocumentoAdquiriente": notaCredito.comprobante.adquiriente.tipoDocumento.codigo,  # DNI
                "NumeroDocumentoAdquiriente": notaCredito.comprobante.adquiriente.numeroDocumento,
                "razonSocial": notaCredito.comprobante.adquiriente.razonSocial
                },
            "taxes" : {},
            "items" : [],
            "documentoRelacionado" : {
                "serieDocumento": notaCredito.comprobante.serie,
                "numeroDocumento": notaCredito.comprobante.numeroComprobante,
                "tipoComprobante": notaCredito.comprobante.tipoComprobante.codigo
                },
            "observaciones" : data["observaciones"],
            "formaPago" : TipoPago.objects.filter(id=data["tipoPago"]).first().name,
            "image_path" : ''
        }
        
        #inicio de la construccion de los datos de emision
        
        #obtener datos de los productos
        
        items = ComprobanteItem.objects.filter(comprobante = notaCredito.comprobante) #ids de los productos necesarios
        sItems = comprobanteItemSerializer(items, many=True).data
        
        try:
            item_ids = [item.codigoItem for item in items]
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
                    "totalTax": 0,
                    "DescripcionItem": item["descripcion"],
                    "id": f"PROD{numeroId}",
                    "precioUnitario": 0,
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
                
                dataToAdd['precioUnitario'] = item['valorUnitario']/(1+totalPercentage)
                
                sendData['comprobante']['cantidadItems'] += cantidad
                sendData['comprobante']['totalConImpuestos'] += item["valorUnitario"] * cantidad
                
                #------------------procesando impuestos-----------------#
                
                for tax in item['taxes']:
                    dataToAdd['tax'][tax['impuesto']['nombre']] = {
                            "operacionesGravadas": round((item['valorUnitario'] * cantidad)/(1+totalPercentage), 2),
                            "MontoTotalImpuesto": round((item['valorUnitario'] * cantidad)-((item['valorUnitario'] * cantidad)/(1+(tax['porcentaje']/100))), 2),
                            "cod1": tax['impuesto']["codigo"],
                            "cod2": tax['impuesto']["nombre"],
                            "cod3": tax['impuesto']["un_ece_5153"],
                            "afectacionIGV": tax['afectacion'],
                    }
                    
                    if sendData['taxes'].get(tax['impuesto']['nombre']):
                        sendData['taxes'][tax['impuesto']['nombre']]['operacionesGravadas'] += round((item['valorUnitario'] * cantidad) / (1 + totalPercentage), 2)
                        sendData['taxes'][tax['impuesto']['nombre']]['MontoTotalImpuesto'] += round((item['valorUnitario'] * cantidad) - ((item['valorUnitario'] * cantidad) / (1 + (tax['porcentaje'] / 100))), 2)
                    else:
                        sendData['taxes'][tax['impuesto']['nombre']] = dataToAdd['tax'][tax['impuesto']['nombre']]
                    
                    totaltax += round((item['valorUnitario'] * cantidad)-((item['valorUnitario'] * cantidad)/(1+(tax['porcentaje']/100))), 2)
                    
                    sendData['comprobante']['MontoTotalImpuestos'] += round((item['valorUnitario'] * cantidad)-((item['valorUnitario'] * cantidad)/(1+(tax['porcentaje']/100))), 2)
            
                dataToAdd['totalTax'] = totaltax
                item_details.append(item)
                sendData['comprobante']["ImporteTotalVenta"] = sendData['comprobante']["totalConImpuestos"] - sendData['comprobante']["MontoTotalImpuestos"] 
                sendData['items'].append(dataToAdd)
                
                generar_notaCredito_url = "http://54.235.246.131:8003//api/nota_credito/"
                response = requests.post(generar_notaCredito_url, json=sendData)
                
                
                
        except requests.RequestException as e:
            return Response({"error": f"Internal API call failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response('hola baby')