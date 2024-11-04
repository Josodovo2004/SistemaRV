from rest_framework import generics
from core.models import Catalogo09TipoNotaDeCredito
from core.serializers import Catalogo09TipoNotaDeCreditoSerializer
from core.filters import Catalogo09TipoNotaDeCreditoFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend

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