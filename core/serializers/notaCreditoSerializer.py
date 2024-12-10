from rest_framework import serializers
from core.models import NotaCredito

class NotaCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaCredito
        fields = ['serie', 'numeroNota', 'comprobante', 'fechaEmision', 'tipo']
