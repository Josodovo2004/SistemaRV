import django_filters
from .models import Entidad, Comprobante

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
    emisor = django_filters.CharFilter(field_name='emisor__razonSocial', lookup_expr='icontains')
    adquiriente = django_filters.CharFilter(field_name='adquiriente__razonSocial', lookup_expr='icontains')
    tipoComprobante = django_filters.CharFilter(field_name='tipoComprobante__nombre', lookup_expr='icontains')
    serie = django_filters.CharFilter(lookup_expr='icontains')
    numeroComprobante = django_filters.CharFilter(lookup_expr='icontains')
    fechaEmision = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Comprobante
        fields = ['emisor', 'adquiriente', 'tipoComprobante', 'serie', 'numeroComprobante', 'fechaEmision']
