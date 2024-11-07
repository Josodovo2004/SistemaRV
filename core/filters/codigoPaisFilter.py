import django_filters
from core.models import CodigoPais

class CodigoPaisFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    pais = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CodigoPais
        fields = ['codigo', 'pais']