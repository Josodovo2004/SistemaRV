from rest_framework import serializers
from core.models import Catalogo01TipoDocumento


class Catalogo01TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo01TipoDocumento
        fields = '__all__'