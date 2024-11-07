import django_filters
from core.models import Ubigeo

class UbigeoFilter(django_filters.FilterSet):
    departamento = django_filters.CharFilter(field_name='ubigeo__departamento', lookup_expr='icontains')
    provincia = django_filters.CharFilter(field_name='ubigeo__provincia', lookup_expr='icontains')
    distrito = django_filters.CharFilter(field_name='ubigeo__distrito', lookup_expr='icontains')
    class Meta:
        model = Ubigeo
        fields = ['departamento', 'provincia', 'distrito']