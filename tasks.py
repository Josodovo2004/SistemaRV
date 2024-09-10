# myapp/tasks.py
from SistemaRV.celery import shared_task, Celery
from core.models import Comprobante, Entidad, ComprobanteItem
from core.serializers import ComprobanteSerializer, ComprobanteItemSerializer
from datetime import date
from .SistemaRV.celery import app

@shared_task
def emisionResumenDeBoletas(data):
    # Your task logic here
    print("This task runs every day at 11:55 PM")

    if data == None:
        #get all boletas from today
        comprobantes = Comprobante.objects.filter(fechaEmision=date.today())
        boletas = [comprobante for comprobante in comprobantes if comprobante.tipoComprobante.codigo == '03']

    # Group boletas by emisor
        grouped_boletas = {}
        for boleta in boletas:
            emisor_id = boleta.emisor.id
            if emisor_id not in grouped_boletas:
                grouped_boletas[emisor_id] = []
            grouped_boletas[emisor_id].append(boleta)

        # Process each group of boletas for each emisor
        for emisor_id, boletas_group in grouped_boletas.items():
            emisor = Entidad.objects.filter(id=emisor_id).first()

            data = {
            'cabecera': {
                'tipo_comprobante': 'RC',
                'serie': '001',
                'correlativo': '00001',
                'fecha_referencia': date.today(),
                'fecha_envio': date.today(),
            },
            'emisor': {
                'ruc': emisor.numeroDocumento,
                'razon_social': emisor.razonSocial,
            },
            'documentos': [],
        }
            for boleta in boletas_group:
                boleta: Comprobante
                itemList = ComprobanteItem.objects.filter(comprobante__id=boleta.id)
                serialized_items= ComprobanteItemSerializer(itemList, many=True)
                
                result: dict = app.send_task('moduloProductos.tasks.darvaloresDeItems', args=[serialized_items]).get()
                result['document_type_code'] = '03'
                result['id'] = f'{boleta.serie}-{boleta.numeroComprobante}'
                result['condition_code'] = '1'
                result['instruction_id'] = '01'
                data['documentos'].append(result)

            # Pass the serialized boletas to the next task
            app.send_task('facturaProject.tasks.emisionDeResumenProgramada', args=[data])