from core.models import Comprobante, Entidad, ComprobanteItem
from datetime import date
from core.serializers import ComprobanteItemSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view # type: ignore
from rest_framework.request import Request
from rest_framework.response import Response
import requests
import json

def emicionDeResumen(*args):
    # Fetching today's comprobantes if not provided

    comprobantes = Comprobante.objects.filter(fechaEmision=date.today())

    # Filtering boletas asynchronously
    boletas = [comprobante for comprobante in comprobantes if comprobante.tipoComprobante.codigo == '03']
    # Grouping boletas by emisor
    grouped_boletas = {}
    for boleta in boletas:
        emisor_id = boleta.emisor.id
        if emisor_id not in grouped_boletas:
            grouped_boletas[emisor_id] = []
        grouped_boletas[emisor_id].append(boleta)

    responses = []
    done = False
    for emisor_id, boletas_group in grouped_boletas.items():
        # Fetch emisor asynchronously
        emisor: Entidad = Entidad.objects.filter(id=emisor_id).first()

        data = {
            'cabecera': {
                'tipo_comprobante': 'RC',
                'serie': '001',
                'correlativo': '00001',
                'fecha_referencia': f'{date.today()}',
                'fecha_envio': f'{date.today()}',
            },
            'emisor': {
                'ruc': emisor.numeroDocumento,
                'razon_social': emisor.razonSocial,
            },
            'documentos': [],
        }
        print(data)

        for boleta in boletas_group:
            try:
                newDocumento = {
                    'id': f'{boleta.serie}-{boleta.numeroComprobante}',
                    'document_type_code': f'{boleta.tipoComprobante.codigo}',
                    'condition_code': '1',
                    'currency': f'{boleta.codigoMoneda.codigo}',
                    'total_amount': 0,
                    'paid_amount': 0,
                    'instruction_id': '01',
                    'tax_amount': 0,
                    'dniComprador': boleta.adquiriente.numeroDocumento,
                }
                tax : dict = {}
                boleta: Comprobante
                # Fetch items asynchronously
                itemList = ComprobanteItem.objects.filter(comprobante__id=boleta.id)
                serialized_items = ComprobanteItemSerializer(itemList, many=True)

                itemData =  serialized_items.data
                print('waiting...')
                newItemData: Response = requests.post('http://localhost:8001/api/resumen/', json=itemData)
                print(newItemData.json())
                
                newItemData = newItemData.json()
                
                for value in newItemData:
                    newDocumento['total_amount'] += value['precioTotal']
                    newDocumento['paid_amount'] += value['precioTotal']
                    for impuesto in value['tax']:
                        if value['tax'][impuesto]['name']  not in tax.keys():
                            tax[impuesto] = value['tax'][impuesto]
                            newDocumento['tax_amount'] += value['tax'][impuesto]['tax_amount']
                        else:
                            tax[impuesto]['tax_amount'] += value['tax'][impuesto]['tax_amount']
                            newDocumento['tax_amount'] += value['tax'][impuesto]['tax_amount']
                newDocumento['tax'] = tax
                
                print(newDocumento)
                
                data['documentos'].append(newDocumento)
            except Exception as e:
                print(e)
        
        sunatResponse: Response = requests.post('http://localhost:8002/api/resumen_diario/', json=data)
        
        if sunatResponse.status_code == 200:
            print(sunatResponse.json())
            return True
        else:
            print(sunatResponse.status_code)
            print(sunatResponse.content)
        
        return True
                
                

if __name__ == '__main__':
    data = {
    'cabecera': {
        'tipo_comprobante': 'RC',  # Type of summary (e.g., "RC" for Resumen de comprobantes)
        'fecha_envio': '2024-10-21',  # The date the summary is sent
        'serie': '001',  # The series number of the summary
        'correlativo': '000123',  # Correlative number of the summary
        'fecha_referencia': '2024-10-20'  # Reference date (the day of the invoices being summarized)
    },
    'emisor': {
        'ruc': '20458765432',  # Issuer's RUC (tax ID)
        'razon_social': 'Empresa Ejemplo S.A.C.'  # Issuer's business name
    },
    'documentos': [
        {
            'id': 'B001-12345',  # Document ID (e.g., invoice or receipt number)
            'document_type_code': '03',  # Document type (e.g., 01 for invoice, 03 for receipt)
            'condition_code': '1',  # Status (e.g., '1' for accepted, '2' for rejected)
            'currency': 'PEN',  # Currency of the document (e.g., PEN for Peruvian Sol)
            'total_amount': '100.00',  # Total amount for the document
            'paid_amount': '100.00',  # Amount paid
            'instruction_id': '01',  # Payment instruction ID
            'tax_amount': '18.00',  # Total tax amount
            'tax': [
                {
                    'id': '1000',  # Tax ID (e.g., "1000" for IGV)
                    'name': 'IGV',  # Tax name
                    'tax_type_code': 'VAT',  # Tax type code (e.g., VAT for value-added tax)
                    'tax_amount': '18.00'  # Tax amount for this line
                }
            ]
        },
        {
            'id': 'B001-12346',
            'document_type_code': '03',
            'condition_code': '1',
            'currency': 'PEN',
            'total_amount': '150.00',
            'paid_amount': '150.00',
            'instruction_id': '01',
            'tax_amount': '27.00',
            'tax': {
                'IGV': {
                    'id': '1000',
                    'name': 'IGV',
                    'tax_type_code': 'VAT',
                    'tax_amount': '27.00'
                }
            }
        }
    ]
}