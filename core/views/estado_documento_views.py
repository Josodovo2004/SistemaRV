from rest_framework import generics
from core.models import EstadoDocumento
from core.serializers import EstadoDocumentoSerializer
from core.filters import EstadoDocumentoFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend

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