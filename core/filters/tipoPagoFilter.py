import django_filters
from core.models import TipoPago

class TipoPagoFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TipoPago
        fields = ['name']