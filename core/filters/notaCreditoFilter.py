import django_filters
from core.models import NotaCredito

class NotaCreditoFilter(django_filters.FilterSet):
    serie = django_filters.CharFilter(lookup_expr='icontains')
    numeroNota = django_filters.CharFilter(lookup_expr='icontains')
    fechaEmision = django_filters.DateFilter(lookup_expr='exact')
    tipo = django_filters.CharFilter(field_name='tipo__codigo', lookup_expr='exact')  # Filter by tipo's codigo

    class Meta:
        model = NotaCredito
        fields = ['serie', 'numeroNota', 'fechaEmision', 'tipo']