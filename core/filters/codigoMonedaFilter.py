import django_filters
from core.models import CodigoMoneda

class CodigoMonedaFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    moneda = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CodigoMoneda
        fields = ['codigo', 'moneda']