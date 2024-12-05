from rest_framework import serializers
from core.models import Ubigeo

class UbigeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubigeo
        fields = '__all__'