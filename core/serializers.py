from rest_framework import serializers # type: ignore
from .models import (
    Catalogo01TipoDocumento,
    Catalogo06DocumentoIdentidad,
    EstadoDocumento,
    Catalogo15ElementosAdicionales,
    Ubigeo,
    CodigoPais,
    CodigoMoneda,
    Entidad,
    Comprobante,
    ComprobanteItem,
    Catalogo51TipoDeOperacion,
    Catalogo09TipoNotaDeCredito,
    Catalogo10TipoNotaDeDebito,
    NotaCredito,
    NotaDebito,
    TipoOperacion,
    TipoPago,
)
import boto3
from django.conf import settings

class Catalogo01TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo01TipoDocumento
        fields = '__all__'

class Catalogo06DocumentoIdentidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo06DocumentoIdentidad
        fields = '__all__'

class EstadoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoDocumento
        fields = '__all__'



class Catalogo15ElementosAdicionalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo15ElementosAdicionales
        fields = '__all__'

class UbigeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubigeo
        fields = '__all__'

class CodigoPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoPais
        fields = '__all__'

class CodigoMonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoMoneda
        fields = '__all__'

class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidad
        fields = '__all__'


class ComprobanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprobante
        fields = '__all__'

class ComprobanteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprobanteItem
        fields = '__all__'
        
        

class Catalogo09TipoNotaDeCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo09TipoNotaDeCredito
        fields = ['codigo', 'descripcion']

class Catalogo10TipoNotaDeDebitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo10TipoNotaDeDebito
        fields = ['codigo', 'descripcion']

class Catalogo51TipoDeOperacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo51TipoDeOperacion
        fields = ['codigo', 'descripcion', 'tipoComprobante']

class NotaCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaCredito
        fields = ['serie', 'numeroNota', 'comprobante', 'fechaEmision', 'tipo']

class NotaDebitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaDebito
        fields = ['serie', 'numeroNota', 'comprobante', 'fechaEmision', 'tipo']
        
        
class TipoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPago
        fields = '__all__'  # Include all fields in the serialization

class TipoOperacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOperacion
        fields = '__all__'  # Include all fields in the serialization