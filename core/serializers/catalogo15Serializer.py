from rest_framework import serializers
from core.models import Catalogo15ElementosAdicionales

class Catalogo15ElementosAdicionalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo15ElementosAdicionales
        fields = '__all__'