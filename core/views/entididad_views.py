from rest_framework import generics
from core.models import Entidad
from core.serializers import EntidadSerializer
from core.filters import EntidadFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from core.models import Ubigeo, CodigoPais, Catalogo06DocumentoIdentidad
from core.serializers import UbigeoSerializer, CodigoPaisSerializer, Catalogo06DocumentoIdentidadSerializer

class EntidadListCreateView(generics.ListCreateAPIView):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = EntidadFilter

class EntidadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

    def retrieve(self, request, *args, **kwargs):
        # Call the original 'retrieve' method to get the default response
        response = super().retrieve(request, *args, **kwargs)

        # Modify the data in the response
        if isinstance(response.data, dict) and 'id' in response.data:
            # Retrieve the Entidad object
            entidad = self.get_object()
            
            # Add nested serialized data to the response
            ubigeo = Ubigeo.objects.filter(codigo= entidad.ubigeo.codigo).first()
            response.data['ubigeo'] = UbigeoSerializer(ubigeo).data
            codigoPais = CodigoPais.objects.filter(codigo= entidad.codigoPais.codigo).first()
            response.data['codigoPais'] = CodigoPaisSerializer(codigoPais).data
            tipoDocumento = Catalogo06DocumentoIdentidad.objects.filter(codigo= entidad.tipoDocumento.codigo).first()
            response.data['tipoDocumento'] = Catalogo06DocumentoIdentidadSerializer(tipoDocumento).data

        # Return the modified response
        return Response(response.data)
    
    @jwt_required
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @jwt_required
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @jwt_required
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)