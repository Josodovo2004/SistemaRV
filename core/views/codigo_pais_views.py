from rest_framework import generics
from core.models import CodigoPais
from core.serializers import CodigoPaisSerializer
from core.filters import CodigoPaisFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend

class CodigoPaisListCreateView(generics.ListCreateAPIView):
    queryset = CodigoPais.objects.all()
    serializer_class = CodigoPaisSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = CodigoPaisFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CodigoPaisRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CodigoPais.objects.all()
    serializer_class = CodigoPaisSerializer
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