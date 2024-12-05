from rest_framework import serializers
from core.models import NotaDebito

class NotaDebitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaDebito
        fields = ['serie', 'numeroNota', 'comprobante', 'fechaEmision', 'tipo']
