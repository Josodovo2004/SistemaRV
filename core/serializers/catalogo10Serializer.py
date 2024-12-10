from rest_framework import serializers
from core.models import Catalogo10TipoNotaDeDebito

class Catalogo10TipoNotaDeDebitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo10TipoNotaDeDebito
        fields = ['codigo', 'descripcion']