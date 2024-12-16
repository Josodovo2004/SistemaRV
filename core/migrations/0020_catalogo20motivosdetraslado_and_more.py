# Generated by Django 4.2.16 on 2024-12-10 15:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_catalogo01tipodocumento_un_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo20MotivosDeTraslado',
            fields=[
                ('codigo', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='comprobanteitem',
            name='porcentajePrecio',
            field=models.FloatField(default=100),
        ),
        migrations.CreateModel(
            name='GuiaRemision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(max_length=4)),
                ('numeroGuia', models.CharField(max_length=8)),
                ('fechaEmision', models.DateField(default=django.utils.timezone.now, null=True)),
                ('emitidoASunat', models.BooleanField(default=False)),
                ('unidadMedida', models.CharField(max_length=15)),
                ('adquirienteGuia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='guias_remision_recibidas', to='core.entidad')),
                ('emisorGuia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='guias_remision_emitidas', to='core.entidad')),
                ('motivoTransporte', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.catalogo20motivosdetraslado')),
            ],
        ),
    ]
