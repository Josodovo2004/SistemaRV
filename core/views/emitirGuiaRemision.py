from rest_framework.response import Response # type: ignore
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from SistemaRV.decorators import jwt_required
from SistemaRV.decorators import CustomJWTAuthentication
from rest_framework.views import APIView
from rest_framework import status
import requests
from core.models import Entidad, Comprobante, ComprobanteItem, TipoPago, GuiaRemision
from core.serializers import comprobanteItemSerializer
