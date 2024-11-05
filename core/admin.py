from django.contrib import admin
from .models import (
    Catalogo01TipoDocumento,
    Catalogo06DocumentoIdentidad,
    EstadoDocumento,
    Catalogo15ElementosAdicionales,
    Ubigeo,
    CodigoPais,
    CodigoMoneda,
    Entidad,
    Comprobante,
    ComprobanteItem,
    Catalogo51TipoDeOperacion,
    Catalogo09TipoNotaDeCredito,
    Catalogo10TipoNotaDeDebito,
    NotaCredito,
    NotaDebito,
    TipoOperacion,
    TipoPago,
)

# Register all models with the Django admin site
admin.site.register(Catalogo01TipoDocumento)
admin.site.register(Catalogo06DocumentoIdentidad)
admin.site.register(EstadoDocumento)
admin.site.register(Catalogo15ElementosAdicionales)
admin.site.register(Ubigeo)
admin.site.register(CodigoPais)
admin.site.register(CodigoMoneda)
admin.site.register(Entidad)
admin.site.register(Comprobante)
admin.site.register(ComprobanteItem)
admin.site.register(Catalogo51TipoDeOperacion)
admin.site.register(Catalogo09TipoNotaDeCredito)
admin.site.register(Catalogo10TipoNotaDeDebito)
admin.site.register(NotaCredito)
admin.site.register(NotaDebito)
admin.site.register(TipoOperacion)
admin.site.register(TipoPago)
