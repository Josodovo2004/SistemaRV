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
import boto3
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

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
    
    

class GeneratePresignedUrlView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

    
    @swagger_auto_schema(
        operation_description="Generate a presigned URL to upload a file to S3. If a file with the same name exists, it will be deleted before generating the URL.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['file_name', 'file_type'],
            properties={
                'file_name': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="The name of the file to be uploaded to S3."
                ),
                'file_type': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="The MIME type of the file (e.g., image/png, application/pdf)."
                ),
            },
        ),
        responses={
            200: openapi.Response(
                description="Presigned URL generated successfully.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'url': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="The generated presigned URL for file upload."
                        ),
                        'file_name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="The name of the file to be uploaded."
                        ),
                    }
                )
            ),
            400: openapi.Response(
                description="Bad Request. Missing file name or file type.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Error message describing the issue."
                        )
                    }
                )
            ),
            500: openapi.Response(
                description="Server Error. Could not check file existence or generate presigned URL.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Error message describing the server error."
                        )
                    }
                )
            ),
        }
    )
    @jwt_required
    def post(self, request):
        file_name = request.data.get('file_name')
        file_type = request.data.get('file_type')

        if not file_name or not file_type:
            return Response({'error': 'File name and file type are required.'}, status=status.HTTP_400_BAD_REQUEST)

        s3_client = boto3.client(
            's3',
            region_name='us-east-1'
        )

        bucket_name = 'qickartbucket'

        # Check if the file exists
        try:
            s3_client.head_object(Bucket=bucket_name, Key=file_name)
            # If it exists, delete the file
            s3_client.delete_object(Bucket=bucket_name, Key=file_name)
        except s3_client.exceptions.ClientError as e:
            if e.response['Error']['Code'] != '404':
                # If the error is something other than "404 Not Found," return an error
                return Response({'error': 'An error occurred while checking for file existence.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Generate the presigned URL for uploading
        try:
            presigned_url = s3_client.generate_presigned_url(
                'put_object',
                Params={
                    'Bucket': bucket_name,
                    'Key': file_name,
                    'ContentType': file_type
                },
                ExpiresIn=120  # URL expiration in seconds
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            'url': presigned_url,
            'file_name': file_name
        }, status=status.HTTP_200_OK)
        
class ConsultarCliente(APIView):
    
    def get(self, request):
        documentNumber = request.GET.get('numero_documento')  # Use request.GET for GET requests

        # Check if the document number is provided
        if not documentNumber:
            return Response({'error': 'Número de documento es requerido'}, status=status.HTTP_400_BAD_REQUEST)

        cliente = get_object_or_404(Entidad, numeroDocumento=documentNumber)
        cliente_data = EntidadSerializer(cliente).data
        
        return Response(cliente_data, status=status.HTTP_200_OK)