from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from core.models import Comprobante, Entidad
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class GetSerieAndNumber(APIView):
    
    @swagger_auto_schema(
        operation_description="Retrieve the next available serie and number for a Comprobante by doc_type and RUC.",
        manual_parameters=[
            openapi.Parameter(
                'doc_type', openapi.IN_QUERY, description="Document type code (e.g., 'B' for Boleta, 'F' for Factura)",
                type=openapi.TYPE_STRING, required=True
            ),
            openapi.Parameter(
                'ruc', openapi.IN_QUERY, description="RUC of the entity issuing the Comprobante",
                type=openapi.TYPE_STRING, required=True
            )
        ],
        responses={
            200: openapi.Response(
                description="Next serie and number for the specified document type and RUC",
                examples={
                    "application/json": {
                        "response": {
                            "serie": "B001",
                            "number": "00000001"
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="Bad Request - missing required parameters",
                examples={
                    "application/json": {
                        "error": "doc_type and ruc are required parameters"
                    }
                }
            ),
            404: openapi.Response(
                description="Not Found - entity with specified RUC not found",
                examples={
                    "application/json": {
                        "detail": "Not found."
                    }
                }
            )
        }
    )
    def get(self, request, *args, **kwargs):
        doc_type = request.query_params.get('doc_type')
        ruc = request.query_params.get('ruc')
        
        # Validate inputs
        if not doc_type or not ruc:
            return Response({"error": "doc_type and ruc are required parameters"}, status=400)
        
        # Find the entity by RUC
        emisor = get_object_or_404(Entidad, numeroDocumento=ruc)
        
        # Get the last Comprobante for this emisor and document type
        last_comprobante = Comprobante.objects.filter(
            emisor=emisor.id,
            tipoComprobante__codigo=doc_type
        ).order_by('-id').first()

        if last_comprobante:
            last_num = int(last_comprobante.numeroComprobante)
            last_serie_suffix = str(last_comprobante.serie)[-2:]
            
            # Check if the last number is at its limit
            if last_num >= 99999999:
                # Reset the number and increment the series suffix
                next_num = 1
                new_serie_number = int(last_serie_suffix) + 1
                serie = f'{last_comprobante.tipoComprobante.serieSufix}{str(new_serie_number).zfill(2)}'
            else:
                # Increment the number within the same series
                next_num = last_num + 1
                serie = last_comprobante.serie
        else:
            # Initialize serie and number if this is the first Comprobante
            serie = f'{doc_type}01'  # Assuming 'doc_type' prefix for series, e.g., 'F001'
            next_num = 1

        # Format the number with leading zeros
        number = str(next_num).zfill(8)
        
        # Return the next serie and number
        return Response({"response": {"serie": serie, "number": number}})
