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
    NotaDebitoListCreateView, NotaDebitoRetrieveUpdateDestroyView,
    Catalogo01TipoDocumentoListCreateView,
    Catalogo01TipoDocumentoRetrieveUpdateDestroyView,
    Catalogo06DocumentoIdentidadListCreateView,
    Catalogo06DocumentoIdentidadRetrieveUpdateDestroyView,
    EstadoDocumentoListCreateView,
    EstadoDocumentoRetrieveUpdateDestroyView,
    Catalogo15ElementosAdicionalesListCreateView,
    Catalogo15ElementosAdicionalesRetrieveUpdateDestroyView,
    CodigoPaisListCreateView,
    CodigoPaisRetrieveUpdateDestroyView,
    CodigoMonedaListCreateView,
    CodigoMonedaRetrieveUpdateDestroyView,
    TipoPagoListCreateView,
    TipoPagoRetrieveUpdateDestroyView,
    TipoOperacionListCreateView,
    TipoOperacionRetrieveUpdateDestroyView,
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
    
     # Catalogo01TipoDocumento URLs
    path('catalogo01/', Catalogo01TipoDocumentoListCreateView.as_view(), name='catalogo01-list-create'),
    path('catalogo01/<pk>/', Catalogo01TipoDocumentoRetrieveUpdateDestroyView.as_view(), name='catalogo01-detail'),

    # Catalogo06DocumentoIdentidad URLs
    path('catalogo06/', Catalogo06DocumentoIdentidadListCreateView.as_view(), name='catalogo06-list-create'),
    path('catalogo06/<pk>/', Catalogo06DocumentoIdentidadRetrieveUpdateDestroyView.as_view(), name='catalogo06-detail'),

    # EstadoDocumento URLs
    path('estado-documento/', EstadoDocumentoListCreateView.as_view(), name='estado-documento-list-create'),
    path('estado-documento/<pk>/', EstadoDocumentoRetrieveUpdateDestroyView.as_view(), name='estado-documento-detail'),

    # Catalogo15ElementosAdicionales URLs
    path('catalogo15/', Catalogo15ElementosAdicionalesListCreateView.as_view(), name='catalogo15-list-create'),
    path('catalogo15/<pk>/', Catalogo15ElementosAdicionalesRetrieveUpdateDestroyView.as_view(), name='catalogo15-detail'),

    # CodigoPais URLs
    path('codigo-pais/', CodigoPaisListCreateView.as_view(), name='codigo-pais-list-create'),
    path('codigo-pais/<pk>/', CodigoPaisRetrieveUpdateDestroyView.as_view(), name='codigo-pais-detail'),

    # CodigoMoneda URLs
    path('codigo-moneda/', CodigoMonedaListCreateView.as_view(), name='codigo-moneda-list-create'),
    path('codigo-moneda/<pk>/', CodigoMonedaRetrieveUpdateDestroyView.as_view(), name='codigo-moneda-detail'),

    # TipoPago URLs
    path('tipo-pago/', TipoPagoListCreateView.as_view(), name='tipo-pago-list-create'),
    path('tipo-pago/<pk>/', TipoPagoRetrieveUpdateDestroyView.as_view(), name='tipo-pago-detail'),

    # TipoOperacion URLs
    path('tipo-operacion/', TipoOperacionListCreateView.as_view(), name='tipo-operacion-list-create'),
    path('tipo-operacion/<pk>/', TipoOperacionRetrieveUpdateDestroyView.as_view(), name='tipo-operacion-detail'),

    # ComprobanteItem URLs
    path('comprobante-item/', ComprobanteItemListCreateView.as_view(), name='comprobante-item-list-create'),
    path('comprobante-item/<pk>/', ComprobanteItemRetrieveUpdateDestroyView.as_view(), name='comprobante-item-detail'),
]