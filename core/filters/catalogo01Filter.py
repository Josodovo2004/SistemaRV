import django_filters
from core.models import Catalogo01TipoDocumento

class Catalogo01TipoDocumentoFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Catalogo01TipoDocumento
        fields = ['codigo', 'descripcion', 'serieSufix']