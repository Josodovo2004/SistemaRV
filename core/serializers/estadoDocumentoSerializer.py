from rest_framework import serializers
from core.models import EstadoDocumento


class EstadoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoDocumento
        fields = '__all__'
