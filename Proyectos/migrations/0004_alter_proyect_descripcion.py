# Generated by Django 5.1.2 on 2024-11-02 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0003_proyect_acabados_proyect_logo_planosproyectos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyect',
            name='descripcion',
            field=models.TextField(default='No tiene una descripcion', max_length=4000),
        ),
    ]
