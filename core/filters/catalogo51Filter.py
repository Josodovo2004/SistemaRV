import django_filters
from core.models import Catalogo51TipoDeOperacion

class Catalogo51TipoDeOperacionFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='exact')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')
    tipoComprobante = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Catalogo51TipoDeOperacion
        fields = ['codigo', 'descripcion', 'tipoComprobante']