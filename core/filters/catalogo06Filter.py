import django_filters
from core.models import Catalogo06DocumentoIdentidad

class Catalogo06DocumentoIdentidadFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Catalogo06DocumentoIdentidad
        fields = ['codigo', 'descripcion', 'abrev']