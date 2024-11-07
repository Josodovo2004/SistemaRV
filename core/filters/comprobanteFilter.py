import django_filters
from core.models import Comprobante


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
