# Generated by Django 4.2.16 on 2024-10-31 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_comprobante_adquiriente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='numeroDocumento',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]