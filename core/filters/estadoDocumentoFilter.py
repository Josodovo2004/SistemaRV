import django_filters
from core.models import EstadoDocumento

class EstadoDocumentoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = EstadoDocumento
        fields = ['nombre']