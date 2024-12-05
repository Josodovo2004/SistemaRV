from rest_framework import serializers
from core.models import Catalogo51TipoDeOperacion

class Catalogo51TipoDeOperacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo51TipoDeOperacion
        fields = ['codigo', 'descripcion', 'tipoComprobante']