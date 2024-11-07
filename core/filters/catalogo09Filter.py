import django_filters
from core.models import Catalogo09TipoNotaDeCredito

class Catalogo09TipoNotaDeCreditoFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='exact')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Catalogo09TipoNotaDeCredito
        fields = ['codigo', 'descripcion']