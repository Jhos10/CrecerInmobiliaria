# Generated by Django 5.1.2 on 2024-11-01 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0002_alter_proyect_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyect',
            name='acabados',
            field=models.TextField(default='No tiene descripcion', max_length=500),
        ),
        migrations.AddField(
            model_name='proyect',
            name='logo',
            field=models.ImageField(default='No tiene icono', upload_to='static/proyectoImages/'),
        ),
        migrations.CreateModel(
            name='PlanosProyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planosImagenes', models.ImageField(default='No tiene planos', upload_to='static/proyectoImages/')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proyectos.proyect')),
            ],
        ),
    ]