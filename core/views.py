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
    NotaDebito,
    Catalogo01TipoDocumento,
    Catalogo06DocumentoIdentidad,
    Catalogo15ElementosAdicionales,
    EstadoDocumento,
    CodigoMoneda,
    CodigoPais,
    TipoOperacion,
    TipoPago,
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
    NotaDebitoSerializer,
    Catalogo01TipoDocumentoSerializer,
    Catalogo06DocumentoIdentidadSerializer,
    Catalogo15ElementosAdicionalesSerializer,
    EstadoDocumentoSerializer,
    CodigoMonedaSerializer,
    CodigoPaisSerializer,
    TipoOperacionSerializer,
    TipoPagoSerializer,
)
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view # type: ignore
from django.http import JsonResponse, Http404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from SistemaRV.decorators import jwt_required
from SistemaRV.decorators import CustomJWTAuthentication
from .filters import (
    EntidadFilter,
    ComprobanteFilter,
    UbigeoFilter,
    Catalogo09TipoNotaDeCreditoFilter,
    Catalogo10TipoNotaDeDebitoFilter,
    Catalogo51TipoDeOperacionFilter,
    NotaCreditoFilter,
    NotaDebitoFilter,
    Catalogo01TipoDocumentoFilter,
    Catalogo06DocumentoIdentidadFilter,
    Catalogo15ElementosAdicionalesFilter,
    TipoOperacionFilter,
    TipoPagoFilter,
    CodigoMonedaFilter,
    CodigoPaisFilter,
    EstadoDocumentoFilter
    )
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
    
    
    

# Catalogo01TipoDocumento Views

class Catalogo01TipoDocumentoListCreateView(generics.ListCreateAPIView):
    queryset = Catalogo01TipoDocumento.objects.all()
    serializer_class = Catalogo01TipoDocumentoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = Catalogo01TipoDocumentoFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class Catalogo01TipoDocumentoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalogo01TipoDocumento.objects.all()
    serializer_class = Catalogo01TipoDocumentoSerializer
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


# Catalogo06DocumentoIdentidad Views

class Catalogo06DocumentoIdentidadListCreateView(generics.ListCreateAPIView):
    queryset = Catalogo06DocumentoIdentidad.objects.all()
    serializer_class = Catalogo06DocumentoIdentidadSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = Catalogo06DocumentoIdentidadFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class Catalogo06DocumentoIdentidadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalogo06DocumentoIdentidad.objects.all()
    serializer_class = Catalogo06DocumentoIdentidadSerializer
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


# EstadoDocumento Views

class EstadoDocumentoListCreateView(generics.ListCreateAPIView):
    queryset = EstadoDocumento.objects.all()
    serializer_class = EstadoDocumentoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = EstadoDocumentoFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class EstadoDocumentoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstadoDocumento.objects.all()
    serializer_class = EstadoDocumentoSerializer
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


# Catalogo15ElementosAdicionales Views

class Catalogo15ElementosAdicionalesListCreateView(generics.ListCreateAPIView):
    queryset = Catalogo15ElementosAdicionales.objects.all()
    serializer_class = Catalogo15ElementosAdicionalesSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = Catalogo15ElementosAdicionalesFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class Catalogo15ElementosAdicionalesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalogo15ElementosAdicionales.objects.all()
    serializer_class = Catalogo15ElementosAdicionalesSerializer
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


# CodigoPais Views

class CodigoPaisListCreateView(generics.ListCreateAPIView):
    queryset = CodigoPais.objects.all()
    serializer_class = CodigoPaisSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = CodigoPaisFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CodigoPaisRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CodigoPais.objects.all()
    serializer_class = CodigoPaisSerializer
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


# CodigoMoneda Views

class CodigoMonedaListCreateView(generics.ListCreateAPIView):
    queryset = CodigoMoneda.objects.all()
    serializer_class = CodigoMonedaSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = CodigoMonedaFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CodigoMonedaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CodigoMoneda.objects.all()
    serializer_class = CodigoMonedaSerializer
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


# TipoPago Views

class TipoPagoListCreateView(generics.ListCreateAPIView):
    queryset = TipoPago.objects.all()
    serializer_class = TipoPagoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = TipoPagoFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TipoPagoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoPago.objects.all()
    serializer_class = TipoPagoSerializer
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


# TipoOperacion Views

class TipoOperacionListCreateView(generics.ListCreateAPIView):
    queryset = TipoOperacion.objects.all()
    serializer_class = TipoOperacionSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = TipoOperacionFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TipoOperacionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoOperacion.objects.all()
    serializer_class = TipoOperacionSerializer
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