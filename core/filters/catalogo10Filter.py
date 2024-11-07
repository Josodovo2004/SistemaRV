import django_filters
from core.models import Catalogo10TipoNotaDeDebito

class Catalogo10TipoNotaDeDebitoFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='exact')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Catalogo10TipoNotaDeDebito
        fields = ['codigo', 'descripcion']