from rest_framework import generics
from core.models import CodigoMoneda
from core.serializers import CodigoMonedaSerializer
from core.filters import CodigoMonedaFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend

class CodigoMonedaListCreateView(generics.ListCreateAPIView):
    queryset = CodigoMoneda.objects.all()
    serializer_class = CodigoMonedaSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = CodigoMonedaFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CodigoMonedaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CodigoMoneda.objects.all()
    serializer_class = CodigoMonedaSerializer
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