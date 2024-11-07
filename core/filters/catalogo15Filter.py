import django_filters
from core.models import Catalogo15ElementosAdicionales

class Catalogo15ElementosAdicionalesFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    tipo = django_filters.CharFilter(lookup_expr='icontains')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Catalogo15ElementosAdicionales
        fields = ['codigo', 'tipo', 'descripcion']