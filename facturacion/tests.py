from django.test import TestCase
from core.models import Comprobante, Entidad, Catalogo01TipoDocumento, CodigoMoneda, CodigoPais, ComprobanteItem, Catalogo06DocumentoIdentidad, Ubigeo
from datetime import date
from asgiref.sync import async_to_sync
from .views import emicionDeResumen

class EmicionResumenTestCase(TestCase):

    def setUp(self):
        self.setup_test_data()

    def setup_test_data(self):
        self.codigoPais = CodigoPais.objects.create(
            codigo='PE',
            pais='Peru'
        )
        Catalogo06DocumentoIdentidad.objects.create(
            codigo=1,
            descripcion='DNI',
            abrev='DNI'
        )
        Catalogo06DocumentoIdentidad.objects.create(
            codigo=6,
            descripcion='RUC',
            abrev='RUC'
        )

        self.ubigeo = Ubigeo.objects.create(
            codigo=160101,
            distrito='Iquitos',
            provincia='Maynas',
            departamento='Loreto',
        )
        self.tipo_comprobante = Catalogo01TipoDocumento.objects.create(
            codigo='03'
        )
        self.codigo_moneda = CodigoMoneda.objects.create(
            codigo='PEN'
        )
        self.emisor = Entidad.objects.create(
            numeroDocumento='20601453269',
            tipoDocumento=Catalogo06DocumentoIdentidad.objects.filter(codigo=6).first(),
            razonSocial='Emisor Test',
            nombreComercial='Emisor Test',
            ubigeo=self.ubigeo,
            direccion='Alzamora 124',
            codigoPais=self.codigoPais,
        )
        self.adquiriente = Entidad.objects.create(
            numeroDocumento='74088718',
            tipoDocumento=Catalogo06DocumentoIdentidad.objects.filter(codigo=1).first(),
            razonSocial='Adquiriente Test',
            nombreComercial='Adquiriente Test',
            ubigeo=self.ubigeo,
            direccion='Alzamora 128',
            codigoPais=self.codigoPais,
        )
        self.comprobante1 = Comprobante.objects.create(
            emisor=self.emisor,
            adquiriente=self.adquiriente,
            tipoComprobante=self.tipo_comprobante,
            serie='001',
            numeroComprobante='00012345',
            fechaEmision=date.today(),
            codigoMoneda=self.codigo_moneda
        )
        self.comprobante2 = Comprobante.objects.create(
            emisor=self.emisor,
            adquiriente=self.adquiriente,
            tipoComprobante=self.tipo_comprobante,
            serie='001',
            numeroComprobante='00012344',
            fechaEmision=date.today(),
            codigoMoneda=self.codigo_moneda
        )
        self.comprobante3 = Comprobante.objects.create(
            emisor=self.emisor,
            adquiriente=self.adquiriente,
            tipoComprobante=self.tipo_comprobante,
            serie='001',
            numeroComprobante='00012346',
            fechaEmision=date.today(),
            codigoMoneda=self.codigo_moneda
        )

        ComprobanteItem.objects.create(
            comprobante=self.comprobante1,
            codigoItem=1,
            cantidad=5
        )
        ComprobanteItem.objects.create(
            comprobante=self.comprobante2,
            codigoItem=1,
            cantidad=5
        )
        ComprobanteItem.objects.create(
            comprobante=self.comprobante3,
            codigoItem=2,
            cantidad=5
        )

    def test_emicionDeResumen(self):
        # Trigger the function directly
        result = async_to_sync(emicionDeResumen)(None)  # Passing None to simulate today's comprobantes

        # Check if the task completed successfully
        self.assertTrue(result, "Function did not complete successfully")

        # Since the function returns True or a list of responses, check if the result is as expected
        if isinstance(result, list):
            self.assertEqual(len(result), 0, "There are unexpected responses")

