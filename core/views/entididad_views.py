from rest_framework import generics
from core.models import Entidad
from core.serializers import EntidadSerializer
from core.filters import EntidadFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from core.serializers import UbigeoSerializer, CodigoPaisSerializer, Catalogo01TipoDocumentoSerializer

class EntidadListCreateView(generics.ListCreateAPIView):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = EntidadFilter

    # Override the list method to customize the GET response
    def list(self, request, *args, **kwargs):
        # Use the default list method to get the response
        response = super().list(request, *args, **kwargs)

        # Check if response.data is a list of dictionaries
        if isinstance(response.data, list):
            for item in response.data:
                if isinstance(item, dict) and 'id' in item:
                    # Safely get the Entidad object and add nested data
                    entidad = self.get_queryset().filter(id=item['id']).first()
                    if entidad:
                        item['ubigeo'] = UbigeoSerializer(entidad.ubigeo).data
                        item['codigoPais'] = CodigoPaisSerializer(entidad.codigoPais).data
                        item['tipoDocumento'] = Catalogo01TipoDocumentoSerializer(entidad.tipoDocumento).data

        return Response(response.data)

class EntidadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer
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