from django.urls import path
from .views import (
    EntidadListCreateView,
    EntidadRetrieveUpdateDestroyView,
    ComprobanteListCreateView,
    ComprobanteRetrieveUpdateDestroyView,
    ComprobanteItemListCreateView,
    ComprobanteItemRetrieveUpdateDestroyView,
    buscar_cliente,
    Catalogo09TipoNotaDeCreditoListCreateView, Catalogo09TipoNotaDeCreditoRetrieveUpdateDestroyView,
    Catalogo10TipoNotaDeDebitoListCreateView, Catalogo10TipoNotaDeDebitoRetrieveUpdateDestroyView,
    Catalogo51TipoDeOperacionListCreateView, Catalogo51TipoDeOperacionRetrieveUpdateDestroyView,
    NotaCreditoListCreateView, NotaCreditoRetrieveUpdateDestroyView,
    NotaDebitoListCreateView, NotaDebitoRetrieveUpdateDestroyView
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

    path('buscar-cliente/', buscar_cliente, name='buscar_cliente'),
    
    path('catalogo09/', Catalogo09TipoNotaDeCreditoListCreateView.as_view(), name='catalogo09-list-create'),
    path('catalogo09/<pk>/', Catalogo09TipoNotaDeCreditoRetrieveUpdateDestroyView.as_view(), name='catalogo09-detail'),
    
    path('catalogo10/', Catalogo10TipoNotaDeDebitoListCreateView.as_view(), name='catalogo10-list-create'),
    path('catalogo10/<pk>/', Catalogo10TipoNotaDeDebitoRetrieveUpdateDestroyView.as_view(), name='catalogo10-detail'),
    
    path('catalogo51/', Catalogo51TipoDeOperacionListCreateView.as_view(), name='catalogo51-list-create'),
    path('catalogo51/<pk>/', Catalogo51TipoDeOperacionRetrieveUpdateDestroyView.as_view(), name='catalogo51-detail'),
    
    path('nota-credito/', NotaCreditoListCreateView.as_view(), name='nota-credito-list-create'),
    path('nota-credito/<pk>/', NotaCreditoRetrieveUpdateDestroyView.as_view(), name='nota-credito-detail'),
    
    path('nota-debito/', NotaDebitoListCreateView.as_view(), name='nota-debito-list-create'),
    path('nota-debito/<pk>/', NotaDebitoRetrieveUpdateDestroyView.as_view(), name='nota-debito-detail'),
]