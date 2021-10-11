# Generated by Django 3.2.8 on 2021-10-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('cedula', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('fecha_Nacimiento', models.CharField(max_length=200)),
                ('celular', models.CharField(max_length=10)),
                ('años_de_Experiencia', models.CharField(max_length=2)),
                ('ultimo_Trabajo', models.CharField(max_length=200)),
                ('costo_Por_Hora', models.CharField(max_length=10)),
                ('clave', models.CharField(max_length=200)),
            ],
        ),
    ]