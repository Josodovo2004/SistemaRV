import csv
from django.core.management.base import BaseCommand
from core.models import Catalogo01TipoDocumento, Catalogo06DocumentoIdentidad, CodigoMoneda, CodigoPais, Ubigeo, TipoOperacion, TipoPago, Catalogo09TipoNotaDeCredito, Catalogo10TipoNotaDeDebito, Catalogo51TipoDeOperacion, EstadoDocumento
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help='Load data from CSV files into the database'
    
    
    
    def handle(self, *args, **options):
        with open('core/management/commands/csv/tipo_moneda.csv', newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                try:
                    if not CodigoMoneda.objects.filter(codigo = row['codigo']).exists():
                        CodigoMoneda.objects.create(codigo=row['codigo'], moneda=row['Moneda'])
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded tipo_moneda data.'))
    
    
        with open('core/management/commands/csv/codigo_pais.csv', newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                try:
                    if not CodigoPais.objects.filter(codigo = row['codigo']).exists():
                        CodigoPais.objects.create(codigo=row['codigo'], pais=row['pais'])
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded codigo_pais data.'))
        
        
        with open('core/management/commands/csv/tipo_comprobante.csv', newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                try:
                    if not Catalogo01TipoDocumento.objects.filter(codigo = row['Codigo']).exists():
                        Catalogo01TipoDocumento.objects.create(codigo=row['Codigo'], descripcion=row['Descripcion'],un_1001=row["UN_1001"],serieSufix=row["serieSufix"])
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded tipo_comprobante data.'))
        

        with open('core/management/commands/csv/tipo_documento.csv', newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                try:
                    if not Catalogo06DocumentoIdentidad.objects.filter(codigo = row['Codigo']).exists():
                        Catalogo06DocumentoIdentidad.objects.create(codigo=row['Codigo'], descripcion=row['Descripcion'],abrev=row["ABREV"])
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded tipo_documento data.'))
        
        with open('core/management/commands/csv/TB_UBIGEOS.csv', newline='') as csvFile:
            reader = csv.DictReader(csvFile, delimiter=';')  # Adjust for semicolon delimiter
            for row in reader:
                try:
                    if not Ubigeo.objects.filter(codigo=row['ubigeo_inei']).exists():
                        Ubigeo.objects.create(
                            codigo=row['ubigeo_inei'], 
                            distrito=row['distrito'], 
                            provincia=row['provincia'], 
                            departamento=row['departamento']
                        )
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded ubigeo data.'))
        
        tipoPagos=['Efectivo', 'Tarjeta', 'Transferencia', 'Movil (Yape,Plin,etc)']
        
        for value in tipoPagos:
            if not TipoPago.objects.filter(name=value).exists():
                TipoPago.objects.create(name=value)
        
        
        tipoOperaciones=['Contado', 'Credito']
        
        for value in tipoOperaciones:
            if not TipoOperacion.objects.filter(name=value).exists():
                TipoOperacion.objects.create(name=value)

        estadoDocumento = ['Emitido', 'Rechazado', 'No Emitido']
        
        for value in estadoDocumento:
            if not EstadoDocumento.objects.filter(nombre=value).exists():
                EstadoDocumento.objects.create(nombre=value)
                
        
        with open('core/management/commands/csv/catalogo09.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    if not Catalogo09TipoNotaDeCredito.objects.filter(codigo=row['codigo']).exists():
                        codigo = row['codigo']
                        descripcion = row['descripcion']

                        # Create or update the record in the database
                        Catalogo09TipoNotaDeCredito.objects.update_or_create(
                            codigo=codigo,
                            defaults={'descripcion': descripcion},
                        )
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded Catalogo09 data'))
        
        with open('core/management/commands/csv/catalogo10.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    if not Catalogo10TipoNotaDeDebito.objects.filter(codigo=row['codigo']).exists():
                        codigo = row['codigo']
                        descripcion = row['descripcion']

                        # Create or update the record in the database
                        Catalogo10TipoNotaDeDebito.objects.update_or_create(
                            codigo=codigo,
                            defaults={'descripcion': descripcion},
                        )
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded Catalogo10 data'))
        
        
        with open('core/management/commands/csv/catalogo51.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    if not Catalogo51TipoDeOperacion.objects.filter(codigo=row['codigo']).exists():
                        codigo = row['codigo']
                        descripcion = row['descripcion']
                        tipoComprobante = row['tipoComprobante']

                        # Create or update the record in the database
                        Catalogo51TipoDeOperacion.objects.update_or_create(
                            codigo=codigo,
                            defaults={'descripcion': descripcion, 'tipoComprobante': tipoComprobante},
                        )
                except IntegrityError:
                    pass

        self.stdout.write(self.style.SUCCESS('Successfully loaded Catalogo51 data'))