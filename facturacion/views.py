# from core.models import Comprobante, Entidad, ComprobanteItem
# from datetime import date
# from core.serializers import ComprobanteItemSerializer
# from celery import Celery
# import logging
# import asyncio
# from asgiref.sync import sync_to_async
# from .consumers import get_response_items, get_response_sunat
# from channels.layers import get_channel_layer
# import logging
# from django.http import HttpResponse

# logger = logging.getLogger(__name__)

# channel_layer = get_channel_layer()

# async def emicionDeResumen(request):
#     response_event = asyncio.Event()

#     def response_handler(event):
#         response_event.set()
#         response = event['message']
#         response_event.response = response

#     # Fetching today's comprobantes if not provided
    
#     comprobantes = await sync_to_async(list)(Comprobante.objects.filter(fechaEmision=date.today()))

#     # Filtering boletas asynchronously
#     boletas = [comprobante for comprobante in comprobantes if (await sync_to_async(lambda: comprobante.tipoComprobante.codigo)()) == '03']
#     # Grouping boletas by emisor
#     grouped_boletas = {}
#     for boleta in boletas:
#         emisor_id = await sync_to_async(lambda: boleta.emisor.id)()
#         if emisor_id not in grouped_boletas:
#             grouped_boletas[emisor_id] = []
#         grouped_boletas[emisor_id].append(boleta)

#     responses = []
#     done = False
#     for emisor_id, boletas_group in grouped_boletas.items():
#         # Fetch emisor asynchronously
#         emisor = await sync_to_async(Entidad.objects.filter(id=emisor_id).first)()

#         data = {
#             'cabecera': {
#                 'tipo_comprobante': 'RC',
#                 'serie': '001',
#                 'correlativo': '00001',
#                 'fecha_referencia': f'{date.today()}',
#                 'fecha_envio': f'{date.today()}',
#             },
#             'emisor': {
#                 'ruc': emisor.numeroDocumento,
#                 'razon_social': emisor.razonSocial,
#             },
#             'documentos': [],
#         }


#         for boleta in boletas_group:
#             try:
#                 # Fetch items asynchronously
#                 itemList = await sync_to_async(list)(ComprobanteItem.objects.filter(comprobante__id=boleta.id))
#                 serialized_items = ComprobanteItemSerializer(itemList, many=True)

#                 data = serialized_items.data

#                 print('waiting...')
#                 # Sending the task to the channel layer
#                 await channel_layer.send(
#                     'ModuloProductos_channel_a',
#                     {
#                     'type': 'process_items',
#                     'items': serialized_items.data,
#                     'response_event' : True,
#                     }
#                 )
                

#                 # You need to have a way to receive the response. This might involve
#                 # listening on a different channel or using a different method to get the result.
#                 # For now, let's assume a placeholder for response handling.
#                 response = await get_response_items()
#                 print('response recieved')
#                 result_data = response

#                 if result_data is None:
#                     logger.error("No response from darvaloresDeItems task")
#                     return HttpResponse("No response from darvaloresDeItems task")
                
#                 result_data['document_type_code'] = '03'
#                 result_data['id'] = f'{boleta.serie}-{boleta.numeroComprobante}'
#                 result_data['condition_code'] = '1'
#                 result_data['instruction_id'] = '01'
#                 data['documentos'].append(result_data)

#             except Exception as e:
#                 logger.error(f"Error processing boleta {boleta.id}: {str(e)}")

#         try:
#             # Sending data to another channel layer task
#             await channel_layer.send(
#                 'facturaProject_channel_a',
#                 {
#                     'type': 'send_bill_resume',
#                     'data': data,
#                     'response_event' : True,
#                 }
#             )

#             response = await get_response_sunat()

#             if response == True:
#                 done= True
#             else:
#                 done= False
#                 responses.append(response)

#         except Exception as e:
#             logger.error(f"Error sending data to emisionDeResumenProgramada: {str(e)}")
#             return HttpResponse(f"Error sending data to emisionDeResumenProgramada: {str(e)}")
        
#     if len(responses) == 0 and done == True:
#         return HttpResponse(True)
#     elif done == False:
#         return HttpResponse('No se envio ningun resumen')
#     else:
#         return HttpResponse(responses)
