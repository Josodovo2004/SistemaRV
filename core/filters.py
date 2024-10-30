import django_filters
from .models import (
    Catalogo01TipoDocumento,
    Catalogo06DocumentoIdentidad,
    EstadoDocumento,
    Catalogo15ElementosAdicionales,
    CodigoPais,
    CodigoMoneda,
    TipoPago,
    TipoOperacion,
    ComprobanteItem,
    Entidad, 
    Comprobante,
    Ubigeo,
    Catalogo09TipoNotaDeCredito,
    Catalogo10TipoNotaDeDebito,
    NotaCredito,
    NotaDebito,
    Catalogo51TipoDeOperacion,
)
class EntidadFilter(django_filters.FilterSet):
    numeroDocumento = django_filters.CharFilter(lookup_expr='icontains')
    razonSocial = django_filters.CharFilter(lookup_expr='icontains')
    nombreComercial = django_filters.CharFilter(lookup_expr='icontains')
    ubigeo = django_filters.CharFilter(field_name='ubigeo__nombre', lookup_expr='icontains')
    direccion = django_filters.CharFilter(lookup_expr='icontains')
    codigoPais = django_filters.CharFilter(field_name='codigoPais__nombre', lookup_expr='icontains')

    class Meta:
        model = Entidad
        fields = ['numeroDocumento', 'razonSocial', 'nombreComercial', 'ubigeo', 'direccion', 'codigoPais']

class ComprobanteFilter(django_filters.FilterSet):
    emisor = django_filters.CharFilter(field_name='emisor__numeroDocumento', lookup_expr='icontains')
    adquiriente = django_filters.CharFilter(field_name='adquiriente__razonSocial', lookup_expr='icontains')
    tipoComprobante = django_filters.CharFilter(field_name='tipoComprobante__nombre', lookup_expr='icontains')
    serie = django_filters.CharFilter(lookup_expr='icontains')
    numeroComprobante = django_filters.CharFilter(lookup_expr='icontains')
    fechaEmision = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Comprobante
        fields = ['emisor', 'adquiriente', 'tipoComprobante', 'serie', 'numeroComprobante', 'fechaEmision']

class UbigeoFilter(django_filters.FilterSet):
    departamento = django_filters.CharFilter(field_name='ubigeo__departamento', lookup_expr='icontains')
    provincia = django_filters.CharFilter(field_name='ubigeo__provincia', lookup_expr='icontains')
    distrito = django_filters.CharFilter(field_name='ubigeo__distrito', lookup_expr='icontains')
    class Meta:
        model = Ubigeo
        fields = ['departamento', 'provincia', 'distrito']
        
class Catalogo09TipoNotaDeCreditoFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='exact')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Catalogo09TipoNotaDeCredito
        fields = ['codigo', 'descripcion']

# Filter for Catalogo10TipoNotaDeDebito
class Catalogo10TipoNotaDeDebitoFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='exact')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Catalogo10TipoNotaDeDebito
        fields = ['codigo', 'descripcion']

# Filter for Catalogo51TipoDeOperacion
class Catalogo51TipoDeOperacionFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='exact')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')
    tipoComprobante = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Catalogo51TipoDeOperacion
        fields = ['codigo', 'descripcion', 'tipoComprobante']

# Filter for NotaCredito
class NotaCreditoFilter(django_filters.FilterSet):
    serie = django_filters.CharFilter(lookup_expr='icontains')
    numeroNota = django_filters.CharFilter(lookup_expr='icontains')
    fechaEmision = django_filters.DateFilter(lookup_expr='exact')
    tipo = django_filters.CharFilter(field_name='tipo__codigo', lookup_expr='exact')  # Filter by tipo's codigo

    class Meta:
        model = NotaCredito
        fields = ['serie', 'numeroNota', 'fechaEmision', 'tipo']

# Filter for NotaDebito
class NotaDebitoFilter(django_filters.FilterSet):
    serie = django_filters.CharFilter(lookup_expr='icontains')
    numeroNota = django_filters.CharFilter(lookup_expr='icontains')
    fechaEmision = django_filters.DateFilter(lookup_expr='exact')
    tipo = django_filters.CharFilter(field_name='tipo__codigo', lookup_expr='exact')  # Filter by tipo's codigo

    class Meta:
        model = NotaDebito
        fields = ['serie', 'numeroNota', 'fechaEmision', 'tipo']
        
        

class Catalogo01TipoDocumentoFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Catalogo01TipoDocumento
        fields = ['codigo', 'descripcion', 'serieSufix']


class Catalogo06DocumentoIdentidadFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Catalogo06DocumentoIdentidad
        fields = ['codigo', 'descripcion', 'abrev']


class EstadoDocumentoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = EstadoDocumento
        fields = ['nombre']


class Catalogo15ElementosAdicionalesFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    tipo = django_filters.CharFilter(lookup_expr='icontains')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Catalogo15ElementosAdicionales
        fields = ['codigo', 'tipo', 'descripcion']


class CodigoPaisFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    pais = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CodigoPais
        fields = ['codigo', 'pais']


class CodigoMonedaFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    moneda = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CodigoMoneda
        fields = ['codigo', 'moneda']


class TipoPagoFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TipoPago
        fields = ['name']


class TipoOperacionFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TipoOperacion
        fields = ['name']


class ComprobanteItemFilter(django_filters.FilterSet):
    codigoItem = django_filters.NumberFilter()
    cantidad = django_filters.NumberFilter()

    class Meta:
        model = ComprobanteItem
        fields = ['codigoItem', 'cantidad']