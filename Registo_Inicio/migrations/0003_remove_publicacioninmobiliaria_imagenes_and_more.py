# Generated by Django 5.1.1 on 2024-09-28 19:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registo_Inicio', '0002_publicacioninmobiliaria_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacioninmobiliaria',
            name='imagenes',
        ),
        migrations.RemoveField(
            model_name='publicacioninmobiliaria',
            name='usuario',
        ),
        migrations.AddField(
            model_name='publicacioninmobiliaria',
            name='imagenPrincipal',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.CreateModel(
            name='ImagenPublicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='images/')),
                ('publicacionInmobiliaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registo_Inicio.publicacioninmobiliaria')),
            ],
        ),
        migrations.CreateModel(
            name='User_PublicacionInmobiliaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacionInmobiliaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registo_Inicio.publicacioninmobiliaria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
