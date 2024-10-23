from rest_framework import generics # type: ignore
from django.http import response
from .models import (
    Entidad,
    Comprobante,
    ComprobanteItem,
    Ubigeo,
    Catalogo09TipoNotaDeCredito, 
    Catalogo10TipoNotaDeDebito,
    Catalogo51TipoDeOperacion, 
    NotaCredito, 
    NotaDebito
)
from .serializers import (
    EntidadSerializer,
    ComprobanteSerializer,
    ComprobanteItemSerializer,
    UbigeoSerializer, 
    Catalogo09TipoNotaDeCreditoSerializer, 
    Catalogo10TipoNotaDeDebitoSerializer, 
    Catalogo51TipoDeOperacionSerializer, 
    NotaCreditoSerializer, 
    NotaDebitoSerializer
)
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view # type: ignore
from django.http import JsonResponse, Http404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from SistemaRV.decorators import jwt_required
from SistemaRV.decorators import CustomJWTAuthentication
from .filters import EntidadFilter, ComprobanteFilter, UbigeoFilter, Catalogo09TipoNotaDeCreditoFilter, Catalogo10TipoNotaDeDebitoFilter, Catalogo51TipoDeOperacionFilter,     NotaCreditoFilter,     NotaDebitoFilter
from django_filters.rest_framework import DjangoFilterBackend
# CRUD views for Entidad

class EntidadListCreateView(generics.ListCreateAPIView):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer
    authentication_classes = [CustomJWTAuthentication]  # Use your custom authentication
    permission_classes = []  # No permission class needed
    filter_backends = [DjangoFilterBackend]
    filterset_class = EntidadFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class EntidadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer
    authentication_classes = [CustomJWTAuthentication]  # Use your custom authentication
    permission_classes = []  # No permission class needed

    @jwt_required
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @jwt_required
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @jwt_required
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# CRUD views for Comprobante
class ComprobanteListCreateView(generics.ListCreateAPIView):
    queryset = Comprobante.objects.all()
    serializer_class = ComprobanteSerializer
    authentication_classes = [CustomJWTAuthentication]  # Use your custom authentication
    permission_classes = []  # No permission class needed
    filter_backends = [DjangoFilterBackend]
    filterset_class = ComprobanteFilter
    
    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ComprobanteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comprobante.objects.all()
    serializer_class = ComprobanteSerializer
    authentication_classes = [CustomJWTAuthentication]  # Use your custom authentication
    permission_classes = []  # No permission class needed

    @jwt_required
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @jwt_required
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @jwt_required
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# CRUD views for ComprobanteItem
class ComprobanteItemListCreateView(generics.ListCreateAPIView):
    queryset = ComprobanteItem.objects.all()
    serializer_class = ComprobanteItemSerializer
    authentication_classes = [CustomJWTAuthentication]  # Use your custom authentication
    permission_classes = []  # No permission class needed

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ComprobanteItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComprobanteItem.objects.all()
    serializer_class = ComprobanteItemSerializer
    authentication_classes = [CustomJWTAuthentication]  # Use your custom authentication
    permission_classes = []  # No permission class needed
    
    @jwt_required
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @jwt_required
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @jwt_required
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class UbigeoListCreateView(generics.ListCreateAPIView):
    queryset = Ubigeo.objects.all()
    serializer_class = UbigeoSerializer
    authentication_classes = [CustomJWTAuthentication]  # Use your custom authentication
    permission_classes = []  # No permission class needed
    filter_backends = [DjangoFilterBackend]
    filterset_class = UbigeoFilter
    
    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


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


# Catalogo09TipoNotaDeCredito Views
class Catalogo09TipoNotaDeCreditoListCreateView(generics.ListCreateAPIView):
    queryset = Catalogo09TipoNotaDeCredito.objects.all()
    serializer_class = Catalogo09TipoNotaDeCreditoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = Catalogo09TipoNotaDeCreditoFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class Catalogo09TipoNotaDeCreditoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalogo09TipoNotaDeCredito.objects.all()
    serializer_class = Catalogo09TipoNotaDeCreditoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

    @jwt_required
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @jwt_required
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @jwt_required
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# Catalogo10TipoNotaDeDebito Views
class Catalogo10TipoNotaDeDebitoListCreateView(generics.ListCreateAPIView):
    queryset = Catalogo10TipoNotaDeDebito.objects.all()
    serializer_class = Catalogo10TipoNotaDeDebitoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = Catalogo10TipoNotaDeDebitoFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class Catalogo10TipoNotaDeDebitoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalogo10TipoNotaDeDebito.objects.all()
    serializer_class = Catalogo10TipoNotaDeDebitoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

    @jwt_required
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @jwt_required
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @jwt_required
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# Catalogo51TipoDeOperacion Views
class Catalogo51TipoDeOperacionListCreateView(generics.ListCreateAPIView):
    queryset = Catalogo51TipoDeOperacion.objects.all()
    serializer_class = Catalogo51TipoDeOperacionSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = Catalogo51TipoDeOperacionFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class Catalogo51TipoDeOperacionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalogo51TipoDeOperacion.objects.all()
    serializer_class = Catalogo51TipoDeOperacionSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

    @jwt_required
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @jwt_required
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @jwt_required
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# NotaCredito Views
class NotaCreditoListCreateView(generics.ListCreateAPIView):
    queryset = NotaCredito.objects.all()
    serializer_class = NotaCreditoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = NotaCreditoFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class NotaCreditoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotaCredito.objects.all()
    serializer_class = NotaCreditoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []


    @jwt_required
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @jwt_required
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @jwt_required
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# NotaDebito Views
class NotaDebitoListCreateView(generics.ListCreateAPIView):
    queryset = NotaDebito.objects.all()
    serializer_class = NotaDebitoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = NotaDebitoFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class NotaDebitoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotaDebito.objects.all()
    serializer_class = NotaDebitoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

    @jwt_required
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @jwt_required
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @jwt_required
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)