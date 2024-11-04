from django.db import models
import django.utils.timezone as tm

# Create your models here.

class Catalogo01TipoDocumento(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=2, primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    un_1001 = models.CharField(db_column='UN_1001', max_length=3, blank=True, null=True)  # Field name made lowercase.
    serieSufix= models.CharField(max_length=2, null=False, default='')

    class Meta:
        db_table = 'CATALOGO_01_TIPO_DOCUMENTO'
    def __str__(self):
        return self.descripcion

class Catalogo06DocumentoIdentidad(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=1, primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    abrev= models.CharField(db_column='ABREV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CATALOGO_06_DOCUMENTO_IDENTIDAD'
    def __str__(self):
        return self.descripcion
    
class EstadoDocumento(models.Model):
    nombre= models.CharField(db_column='nombre',  max_length=50,null=True)
    class Meta:
        db_table = 'ESTADO_DOCUMENTO'
    def __str__(self):
        return self.nombre

class Catalogo15ElementosAdicionales(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=4,primary_key =True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CATALOGO_15_ELEMENTOS_ADICIONALES'

class Catalogo09TipoNotaDeCredito(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=2,primary_key =True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    
class Catalogo10TipoNotaDeDebito(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=2,primary_key =True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.

class Catalogo51TipoDeOperacion(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=4,primary_key =True, default='')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tipoComprobante = models.CharField(max_length=100, null=True)

class Ubigeo(models.Model):
    codigo = models.CharField(max_length=10, null=False)
    distrito = models.CharField(max_length=100, null=False)
    provincia = models.CharField(max_length=100, null=False)
    departamento = models.CharField(max_length=100, null=False)
    def __str__(self) -> str:
        return f'{self.distrito} {self.provincia} {self.departamento}'

class CodigoPais(models.Model):
    codigo = models.CharField(max_length=5, null=False)
    pais = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return f'{self.pais}'

class CodigoMoneda(models.Model):
    codigo = models.CharField(max_length=4, null=False)
    moneda = models.CharField(max_length=50, null=False)
    
    def __str__(self) -> str:
        return self.moneda

class Entidad(models.Model):
    numeroDocumento = models.CharField(max_length=11, null=False, unique=False)
    tipoDocumento = models.ForeignKey(Catalogo06DocumentoIdentidad, on_delete=models.CASCADE, null=False)
    razonSocial = models.CharField(max_length=150, null=False)
    nombreComercial = models.CharField(max_length=150, null=True)
    celular = models.CharField(max_length=15, null=True)
    ubigeo = models.ForeignKey(Ubigeo, on_delete=models.CASCADE, null=False)
    direccion = models.CharField(max_length=50, null=False)
    codigoPais = models.ForeignKey(CodigoPais, on_delete=models.CASCADE, null=False)
    imagen = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.nombreComercial

class TipoPago(models.Model):
    name= models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.name

class TipoOperacion(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comprobante(models.Model):
    emisor = models.ForeignKey(Entidad, on_delete=models.DO_NOTHING, null=False, related_name='comprobantes_emitidos')
    adquiriente = models.ForeignKey(Entidad, on_delete=models.DO_NOTHING, null=True, related_name='comprobantes_recibidos')
    tipoComprobante = models.ForeignKey(Catalogo01TipoDocumento, on_delete=models.DO_NOTHING, null=False)
    tipoOperacion = models.ForeignKey(Catalogo51TipoDeOperacion, on_delete=models.DO_NOTHING, null=True)
    tipoPago = models.ForeignKey(TipoPago, on_delete=models.DO_NOTHING, null=True)
    serie = models.CharField(max_length=4, null=False)
    numeroComprobante = models.CharField(max_length=8, null=False)
    fechaEmision = models.DateField(default=tm.now, null=True)
    codigoMoneda = models.ForeignKey(CodigoMoneda, on_delete=models.DO_NOTHING, null=True)
    estado = models.ForeignKey(EstadoDocumento, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        emisor_name = str(self.emisor.razonSocial) if self.emisor and self.emisor.razonSocial else "Unknown"
        adquiriente_name = str(self.adquiriente.razonSocial) if self.adquiriente and self.adquiriente.razonSocial else "Unknown"
        fecha_emision = str(self.fechaEmision) if self.fechaEmision else "NoDate"
        serie = str(self.serie) if self.serie else "null"
        numero = str(self.numeroComprobante) if self.numeroComprobante else "null"
        return f"{emisor_name}-{serie}-{numero}"
    
    def save(self, *args, **kwargs):
        if not self.serie or not self.numeroComprobante:
            # Get the last issued Comprobante
            last_comprobante = Comprobante.objects.filter(serie__startswith=self.tipoComprobante.codigo, emisor__id = self.emisor.id).order_by('-id').first()

            if last_comprobante:
                last_num = int(last_comprobante.numeroComprobante)
                last_serie = str(last_comprobante.serie)[-2::]
                
                # Check if the number is at its limit
                if last_num >= 99999999:
                    # Reset numeroComprobante and increment serie
                    last_num = 1
                    # Increment series (e.g., from F001 to F002, or B001 to B002)
                    new_serie_number = int(last_serie) + 1
                    self.serie = str(new_serie_number).zfill(2)
                else:
                    last_num += 1
                    self.serie = last_serie
            else:
                # Initialize serie and numeroComprobante if this is the first record
                self.serie = f'{self.tipoComprobante.serieSufix}01'  # Example: F001 or B001
                last_num = 1

            self.numeroComprobante = str(last_num).zfill(8)
        super().save(*args, **kwargs)

class ComprobanteItem(models.Model):
    comprobante = models.ForeignKey(Comprobante, on_delete=models.CASCADE ,null=False)
    codigoItem = models.IntegerField(null=False)
    cantidad = models.IntegerField(null=False)
    
class NotaCredito(models.Model):
    serie = models.CharField(max_length=4, null=False)
    numeroNota = models.CharField(max_length=8, null=False)
    comprobante = models.ForeignKey(Comprobante, on_delete=models.DO_NOTHING)
    fechaEmision = models.DateField(default=tm.now, null=True)
    tipo = models.ForeignKey(Catalogo09TipoNotaDeCredito, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f'Nota de credito: {self.serie}-{self.numeroNota}'
    
    def save(self, *args, **kwargs):
        if not self.serie or not self.numeroComprobante:
            # Get the last issued Comprobante
            last_comprobante = Comprobante.objects.filter(serie__startswith=self.tipoComprobante.codigo, emisor__id = self.emisor.id).order_by('-id').first()

            if last_comprobante:
                last_num = int(last_comprobante.numeroComprobante)
                last_serie = str(last_comprobante.serie)[-2::]
                
                # Check if the number is at its limit
                if last_num >= 99999999:
                    # Reset numeroComprobante and increment serie
                    last_num = 1
                    # Increment series (e.g., from F001 to F002, or B001 to B002)
                    new_serie_number = int(last_serie) + 1
                    self.serie = str(new_serie_number).zfill(2)
                else:
                    last_num += 1
                    self.serie = last_serie
            else:
                # Initialize serie and numeroComprobante if this is the first record
                self.serie = f'{self.comprobante.tipoComprobante.serieSufix}N01'  # Example: F001 or B001
                last_num = 1

            self.numeroComprobante = str(last_num).zfill(8)
        super().save(*args, **kwargs)

class NotaDebito(models.Model):
    serie = models.CharField(max_length=4, null=False)
    numeroNota = models.CharField(max_length=8, null=False)
    comprobante = models.ForeignKey(Comprobante, on_delete=models.DO_NOTHING)
    fechaEmision = models.DateField(default=tm.now, null=True)
    tipo = models.ForeignKey(Catalogo10TipoNotaDeDebito, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f'Nota de credito: {self.serie}-{self.numeroNota}'
    
    def save(self, *args, **kwargs):
        if not self.serie or not self.numeroComprobante:
            # Get the last issued Comprobante
            last_comprobante = Comprobante.objects.filter(serie__startswith=self.tipoComprobante.codigo, emisor__id = self.emisor.id).order_by('-id').first()

            if last_comprobante:
                last_num = int(last_comprobante.numeroComprobante)
                last_serie = str(last_comprobante.serie)[-2::]
                
                # Check if the number is at its limit
                if last_num >= 99999999:
                    # Reset numeroComprobante and increment serie
                    last_num = 1
                    # Increment series (e.g., from F001 to F002, or B001 to B002)
                    new_serie_number = int(last_serie) + 1
                    self.serie = str(new_serie_number).zfill(2)
                else:
                    last_num += 1
                    self.serie = last_serie
            else:
                # Initialize serie and numeroComprobante if this is the first record
                self.serie = f'{self.comprobante.tipoComprobante.serieSufix}N01'  # Example: F001 or B001
                last_num = 1

            self.numeroComprobante = str(last_num).zfill(8)
        super().save(*args, **kwargs)