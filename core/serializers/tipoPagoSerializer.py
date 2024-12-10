from rest_framework import serializers
from core.models import TipoPago

class TipoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPago
        fields = '__all__'  # Include all fields in the serialization