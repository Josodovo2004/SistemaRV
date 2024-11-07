import django_filters
from core.models import Entidad

class EntidadFilter(django_filters.FilterSet):
    numeroDocumento = django_filters.CharFilter(lookup_expr='icontains')
    razonSocial = django_filters.CharFilter(lookup_expr='icontains')
    nombreComercial = django_filters.CharFilter(lookup_expr='icontains')
    ubigeo = django_filters.CharFilter(field_name='ubigeo__codigo', lookup_expr='icontains')
    direccion = django_filters.CharFilter(lookup_expr='icontains')
    codigoPais = django_filters.CharFilter(field_name='codigoPais__pais', lookup_expr='icontains')

    class Meta:
        model = Entidad
        fields = ['numeroDocumento', 'razonSocial', 'nombreComercial', 'ubigeo', 'direccion', 'codigoPais']
