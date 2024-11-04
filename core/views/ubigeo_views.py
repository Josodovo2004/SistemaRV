from rest_framework import generics
from core.models import Ubigeo
from core.serializers import UbigeoSerializer
from core.filters import UbigeoFilter
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend


class UbigeoListCreateView(generics.ListCreateAPIView):
    queryset = Ubigeo.objects.all()
    serializer_class = UbigeoSerializer
    authentication_classes = [CustomJWTAuthentication]  
    permission_classes = [] 
    filter_backends = [DjangoFilterBackend]
    filterset_class = UbigeoFilter
    
    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)