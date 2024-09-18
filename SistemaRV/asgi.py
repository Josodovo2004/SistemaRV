import os
from django.core.asgi import get_asgi_application
from facturacion import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SistemaRV.settings')

application = get_asgi_application()