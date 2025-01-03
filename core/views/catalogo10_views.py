from rest_framework import generics
from core.models import Catalogo10TipoNotaDeDebito
from core.serializers import Catalogo10TipoNotaDeDebitoSerializer
from core.filters import Catalogo10TipoNotaDeDebitoFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend


class Catalogo10TipoNotaDeDebitoListCreateView(generics.ListCreateAPIView):
    queryset = Catalogo10TipoNotaDeDebito.objects.all()
    serializer_class = Catalogo10TipoNotaDeDebitoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = Catalogo10TipoNotaDeDebitoFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class Catalogo10TipoNotaDeDebitoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalogo10TipoNotaDeDebito.objects.all()
    serializer_class = Catalogo10TipoNotaDeDebitoSerializer
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