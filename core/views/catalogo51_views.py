from rest_framework import generics
from core.models import Catalogo51TipoDeOperacion
from core.serializers import Catalogo51TipoDeOperacionSerializer
from core.filters import Catalogo51TipoDeOperacionFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend

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