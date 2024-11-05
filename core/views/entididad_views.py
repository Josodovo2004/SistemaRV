from rest_framework import generics
from core.models import Entidad
from core.serializers import EntidadSerializer
from core.filters import EntidadFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from core.models import Ubigeo, CodigoPais, Catalogo01TipoDocumento
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
        # Call the original 'list' method to get the default response
        response = super().list(request, *args, **kwargs)

        # Modify the data in the response
        if isinstance(response.data, list):
            for item in response.data:
                if isinstance(item, dict) and 'id' in item:
                    # Retrieve the Entidad object
                    entidad = self.get_queryset().filter(id=item['id']).first()
                    if entidad:
                        # Add nested serialized data to the response
                        ubigeo = Ubigeo.objects.filter(id= entidad.ubigeo).first()
                        item['ubigeo'] = UbigeoSerializer(ubigeo).data
                        codigoPais = CodigoPais.objects.filter(id= entidad.codigoPais).first()
                        item['codigoPais'] = CodigoPaisSerializer(codigoPais).data
                        tipoDocumento = Catalogo01TipoDocumento.objects.filter(id= entidad.tipoDocumento).first()
                        item['tipoDocumento'] = Catalogo01TipoDocumentoSerializer(tipoDocumento).data

        # Return the modified response
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