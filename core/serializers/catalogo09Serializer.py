from rest_framework import serializers
from core.models import Catalogo09TipoNotaDeCredito

class Catalogo09TipoNotaDeCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo09TipoNotaDeCredito
        fields = ['codigo', 'descripcion']