import django_filters
from core.models import ComprobanteItem

class ComprobanteItemFilter(django_filters.FilterSet):
    codigoItem = django_filters.NumberFilter()
    cantidad = django_filters.NumberFilter()

    class Meta:
        model = ComprobanteItem
        fields = ['codigoItem', 'cantidad']