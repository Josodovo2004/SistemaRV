from rest_framework import generics # type: ignore
from django.http import response
from .models import (
    Entidad,
    Comprobante,
    ComprobanteItem
)
from .serializers import (
    EntidadSerializer,
    ComprobanteSerializer,
    ComprobanteItemSerializer
)
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view # type: ignore
from django.http import JsonResponse, Http404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# CRUD views for Entidad
class EntidadListCreateView(generics.ListCreateAPIView):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer

class EntidadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer

# CRUD views for Comprobante
class ComprobanteListCreateView(generics.ListCreateAPIView):
    queryset = Comprobante.objects.all()
    serializer_class = ComprobanteSerializer

class ComprobanteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comprobante.objects.all()
    serializer_class = ComprobanteSerializer

# CRUD views for ComprobanteItem
class ComprobanteItemListCreateView(generics.ListCreateAPIView):
    queryset = ComprobanteItem.objects.all()
    serializer_class = ComprobanteItemSerializer

class ComprobanteItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComprobanteItem.objects.all()
    serializer_class = ComprobanteItemSerializer




@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'numeroDocumento': openapi.Schema(type=openapi.TYPE_STRING, description='Número de Documento del cliente'),
        },
        required=['numeroDocumento'],
    ),
    responses={
        200: EntidadSerializer(),
        404: 'No Encontrado',
        400: 'Bad Request',
    }
)
@api_view(['POST'])
def buscar_cliente(request):
    try:
        data: dict = request.data  
        nDocumento = data.get('numeroDocumento')  

        # Buscar el cliente
        cliente = Entidad.objects.filter(numeroDocumento=nDocumento).first()

        if cliente is None:
            return JsonResponse({'No Encontrado'}, status=404)


        # Serializar los datos del cliente
        serializer = EntidadSerializer(cliente)
        return Response(serializer.data, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)