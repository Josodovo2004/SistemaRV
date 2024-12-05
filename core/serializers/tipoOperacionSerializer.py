from rest_framework import serializers
from core.models import TipoOperacion

class TipoOperacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOperacion
        fields = '__all__'  # Include all fields in the serialization