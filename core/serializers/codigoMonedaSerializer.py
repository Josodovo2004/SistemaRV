from rest_framework import serializers
from core.models import CodigoMoneda

class CodigoMonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoMoneda
        fields = '__all__'