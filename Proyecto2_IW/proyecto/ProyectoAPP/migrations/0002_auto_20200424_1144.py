# Generated by Django 3.0.5 on 2020-04-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]