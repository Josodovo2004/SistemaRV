from rest_framework import serializers # type: ignore
from .models import (
    Catalogo01TipoDocumento,
    Catalogo06DocumentoIdentidad,
    EstadoDocumento,
    Usuario,
    Cliente,
    
    Catalogo15ElementosAdicionales,
    Ubigeo,
    CodigoPais,
    CodigoMoneda,
    Entidad,
    Comprobante,
    ComprobanteItem,
)
import boto3
from django.conf import settings

class Catalogo01TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo01TipoDocumento
        fields = '__all__'

class Catalogo06DocumentoIdentidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo06DocumentoIdentidad
        fields = '__all__'

class EstadoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoDocumento
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'



class Catalogo15ElementosAdicionalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo15ElementosAdicionales
        fields = '__all__'

class UbigeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubigeo
        fields = '__all__'

class CodigoPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoPais
        fields = '__all__'

class CodigoMonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoMoneda
        fields = '__all__'

class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidad
        fields = '__all__'
        
    def upload_image_to_s3(self, image, nombre_comercial):
        # Generate S3 client
        s3= boto3.client(
            's3',
            region_name=settings.AWS_S3_REGION_NAME
        )
        
        # Format the file name using the `nombreComercial`
        file_name = f"entidades/{nombre_comercial}_{image.name}"  # You can customize the file path here
        
        # Upload the image to S3
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        s3.upload_fileobj(image, bucket_name, file_name)
        
        # Generate the S3 URL
        file_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
        
        return file_url

    def create(self, validated_data):
        # Check if an image is provided
        image = validated_data.pop('imagen', None)
        
        # Create the Entidad instance first without the image
        entidad = Entidad.objects.create(**validated_data)
        
        # If an image is present, upload it to S3
        if image:
            # Use the `nombreComercial` for the image file name
            image_url = self.upload_image_to_s3(image, entidad.nombreComercial)
            entidad.imagen = image_url  # Update the `imagen` field with the S3 URL
            entidad.save()  # Save the changes to the database
        
        return entidad


class ComprobanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprobante
        fields = '__all__'

class ComprobanteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprobanteItem
        fields = '__all__'