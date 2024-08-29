from django.urls import path
from .views import (
    EntidadListCreateView,
    EntidadRetrieveUpdateDestroyView,
    ComprobanteListCreateView,
    ComprobanteRetrieveUpdateDestroyView,
    ComprobanteItemListCreateView,
    ComprobanteItemRetrieveUpdateDestroyView,
)

urlpatterns = [
    # URLs for Entidad
    path('entidades/', EntidadListCreateView.as_view(), name='entidad-list-create'),
    path('entidades/<int:pk>/', EntidadRetrieveUpdateDestroyView.as_view(), name='entidad-retrieve-update-destroy'),

    # URLs for Comprobante
    path('comprobantes/', ComprobanteListCreateView.as_view(), name='comprobante-list-create'),
    path('comprobantes/<int:pk>/', ComprobanteRetrieveUpdateDestroyView.as_view(), name='comprobante-retrieve-update-destroy'),

    # URLs for ComprobanteItem
    path('comprobante-items/', ComprobanteItemListCreateView.as_view(), name='comprobante-item-list-create'),
    path('comprobante-items/<int:pk>/', ComprobanteItemRetrieveUpdateDestroyView.as_view(), name='comprobante-item-retrieve-update-destroy'),
]