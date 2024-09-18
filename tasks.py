from celery import shared_task
from facturacion.views import emicionDeResumen
import logging

logger = logging.getLogger(__name__)

@shared_task
def emisionResumenDeBoletas(comprobantes=None):
    try:
        # Process comprobantes (your existing logic here)
        result = emicionDeResumen(comprobantes)

        if result == True:
            logger.info('Boletas Emitidas exitosamente')
        else:
            logger.error(f'Error details: {result}')
    except Exception as e:
        logger.error(f'Error in emisionResumenDeBoletas: {str(e)}')
