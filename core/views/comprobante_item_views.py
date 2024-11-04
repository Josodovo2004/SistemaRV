from rest_framework import generics
from core.models import ComprobanteItem
from core.serializers import ComprobanteItemSerializer
from core.filters import ComprobanteFilter
from rest_framework.permissions import AllowAny
from SistemaRV.decorators import jwt_required, CustomJWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend


class ComprobanteItemListCreateView(generics.ListCreateAPIView):
    queryset = ComprobanteItem.objects.all()
    serializer_class = ComprobanteItemSerializer
    authentication_classes = [CustomJWTAuthentication]  # Use your custom authentication
    permission_classes = []  # No permission class needed

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ComprobanteItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComprobanteItem.objects.all()
    serializer_class = ComprobanteItemSerializer
    authentication_classes = [CustomJWTAuthentication]  # Use your custom authentication
    permission_classes = []  # No permission class needed
    
    @jwt_required
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @jwt_required
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @jwt_required
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)