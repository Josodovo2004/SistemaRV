import django_filters
from core.models import TipoOperacion

class TipoOperacionFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TipoOperacion
        fields = ['name']