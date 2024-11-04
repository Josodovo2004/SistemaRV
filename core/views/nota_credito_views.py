from rest_framework import generics
from core.models import NotaCredito
from core.serializers import NotaCreditoSerializer
from core.filters import NotaCreditoFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend

# NotaCredito Views
class NotaCreditoListCreateView(generics.ListCreateAPIView):
    queryset = NotaCredito.objects.all()
    serializer_class = NotaCreditoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = NotaCreditoFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class NotaCreditoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotaCredito.objects.all()
    serializer_class = NotaCreditoSerializer
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