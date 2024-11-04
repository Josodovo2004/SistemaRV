from rest_framework import generics
from core.models import Catalogo15ElementosAdicionales
from core.serializers import Catalogo15ElementosAdicionalesSerializer
from core.filters import Catalogo15ElementosAdicionalesFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend

class Catalogo15ElementosAdicionalesListCreateView(generics.ListCreateAPIView):
    queryset = Catalogo15ElementosAdicionales.objects.all()
    serializer_class = Catalogo15ElementosAdicionalesSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = Catalogo15ElementosAdicionalesFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class Catalogo15ElementosAdicionalesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalogo15ElementosAdicionales.objects.all()
    serializer_class = Catalogo15ElementosAdicionalesSerializer
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