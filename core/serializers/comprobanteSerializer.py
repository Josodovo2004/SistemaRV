from rest_framework import serializers
from core.models import Comprobante

class ComprobanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprobante
        fields = '__all__'