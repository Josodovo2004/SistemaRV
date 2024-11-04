from rest_framework import generics
from core.models import Catalogo01TipoDocumento
from core.serializers import Catalogo01TipoDocumentoSerializer
from core.filters import Catalogo01TipoDocumentoFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend


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