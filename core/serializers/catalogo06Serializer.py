from rest_framework import serializers
from core.models import Catalogo06DocumentoIdentidad


class Catalogo06DocumentoIdentidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo06DocumentoIdentidad
        fields = '__all__'
