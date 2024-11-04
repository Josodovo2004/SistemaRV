from rest_framework.response import Response # type: ignore
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from SistemaRV.decorators import jwt_required
from SistemaRV.decorators import CustomJWTAuthentication
from rest_framework.views import APIView
from rest_framework import status
from core.serializers import EntidadSerializer
from core.models import Entidad
from django.shortcuts import get_object_or_404

class ConsultarCliente(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    
    @swagger_auto_schema(
        operation_description="Consulta un cliente por número de documento.",
        manual_parameters=[
            openapi.Parameter(
                'numero_documento', 
                openapi.IN_QUERY, 
                description="Número de documento del cliente", 
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            200: openapi.Response(
                description="Datos del cliente",
                schema=EntidadSerializer(),  # Ensure EntidadSerializer is a valid schema
            ),
            400: openapi.Response(
                description="Error: Número de documento es requerido",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, description='Mensaje de error'),
                    }
                ),
            ),
            404: openapi.Response(
                description="Error: Cliente no encontrado",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, description='Mensaje de error'),
                    }
                ),
            ),
        }
    )
    @jwt_required
    def get(self, request):
        documentNumber = request.GET.get('numero_documento')  # Use request.GET for GET requests

        # Check if the document number is provided
        if not documentNumber:
            return Response({'error': 'Número de documento es requerido'}, status=status.HTTP_400_BAD_REQUEST)

        cliente = get_object_or_404(Entidad, numeroDocumento=documentNumber)
        cliente_data = EntidadSerializer(cliente).data
        
        return Response(cliente_data, status=status.HTTP_200_OK)