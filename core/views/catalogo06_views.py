from rest_framework import generics
from core.models import Catalogo06DocumentoIdentidad
from core.serializers import Catalogo06DocumentoIdentidadSerializer
from core.filters import Catalogo06DocumentoIdentidadFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend

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