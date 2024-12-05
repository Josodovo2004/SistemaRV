from rest_framework import serializers
from core.models import CodigoPais

class CodigoPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoPais
        fields = '__all__'