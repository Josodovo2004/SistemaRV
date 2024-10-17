 from core.models import Comprobante, Entidad, ComprobanteItem
 from datetime import date
 from core.serializers import ComprobanteItemSerializer
 from django.http import HttpResponse
 from rest_framework.decorators import api_view # type: ignore

@api_view(['POST'])
def emicionDeResumen(request):

    def response_handler(event):
        response_event.set()
        response = event['message']
        response_event.response = response

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
        emisor: Entidad = Entidad.objects.filter(id=emisor_id).first

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


        for boleta in boletas_group:
            try:
                # Fetch items asynchronously
                itemList = ComprobanteItem.objects.filter(comprobante__id=boleta.id)
                serialized_items = ComprobanteItemSerializer(itemList, many=True)

                data = serialized_items.data

                print('waiting...')
                