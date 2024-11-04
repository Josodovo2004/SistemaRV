from rest_framework import generics
from core.models import NotaDebito
from core.serializers import NotaDebitoSerializer
from core.filters import NotaDebitoFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend

class NotaDebitoListCreateView(generics.ListCreateAPIView):
    queryset = NotaDebito.objects.all()
    serializer_class = NotaDebitoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = NotaDebitoFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class NotaDebitoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotaDebito.objects.all()
    serializer_class = NotaDebitoSerializer
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