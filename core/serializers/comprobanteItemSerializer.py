from rest_framework import serializers
from core.models import ComprobanteItem

class ComprobanteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprobanteItem
        fields = '__all__'