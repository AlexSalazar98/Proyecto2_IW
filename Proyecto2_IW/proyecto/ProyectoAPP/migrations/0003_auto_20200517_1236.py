# Generated by Django 3.0.5 on 2020-05-17 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoAPP', '0002_auto_20200517_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='nombre',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
