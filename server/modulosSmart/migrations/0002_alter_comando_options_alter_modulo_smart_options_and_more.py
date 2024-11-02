# Generated by Django 5.0.2 on 2024-11-01 22:00

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulosSmart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comando',
            options={'verbose_name': 'Comandos IR'},
        ),
        migrations.AlterModelOptions(
            name='modulo_smart',
            options={'verbose_name': 'Modulo Smart IF'},
        ),
        migrations.AlterModelOptions(
            name='registro_uso',
            options={'verbose_name': 'Registro Uso'},
        ),
        migrations.AlterModelOptions(
            name='sala',
            options={'verbose_name': 'Salas - Laboratorio'},
        ),
        migrations.AlterModelOptions(
            name='setor',
            options={'verbose_name': 'Setor'},
        ),
        migrations.AlterModelOptions(
            name='tipo',
            options={'verbose_name': 'Tipo do Dispositivo'},
        ),
        migrations.AlterModelOptions(
            name='tipo_user',
            options={'verbose_name': 'Tipo de Usuario'},
        ),
        migrations.AddField(
            model_name='dispositivos',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='modulo_smart',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='modulo_smart',
            name='temperatura',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modulo_smart',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comando',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dispositivos',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='modulo_smart',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registro_uso',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sala',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='setor',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nivel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='modulosSmart.tipo_user'),
        ),
    ]