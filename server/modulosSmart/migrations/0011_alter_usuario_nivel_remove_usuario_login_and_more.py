# Generated by Django 5.0.2 on 2024-12-16 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulosSmart', '0010_dispositivos_atual_temperatura_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nivel',
            field=models.CharField(choices=[('Professor', 'Professor'), ('Coordenação de turma', 'Coordenação de turma')], max_length=100),
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='login',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='senha',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='matricula',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Tipo_user',
        ),
    ]