# Generated by Django 5.1.1 on 2024-09-29 02:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registo_Inicio', '0003_remove_publicacioninmobiliaria_imagenes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenpublicacion',
            name='imagen',
            field=models.ImageField(upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='publicacioninmobiliaria',
            name='imagenPrincipal',
            field=models.ImageField(default=None, upload_to='static/images/'),
        ),
        migrations.CreateModel(
            name='VideoPublicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.FileField(upload_to='static/videosPublicaciones')),
                ('publicacionInmobiliaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registo_Inicio.publicacioninmobiliaria')),
            ],
        ),
    ]
