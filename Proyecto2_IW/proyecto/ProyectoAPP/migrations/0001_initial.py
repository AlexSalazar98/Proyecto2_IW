# Generated by Django 3.0.5 on 2020-04-10 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('empresa', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('localizacion', models.TextField()),
                ('telefono', models.IntegerField()),
                ('numero_cuenta', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(default='Abierta', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('apellido1', models.CharField(max_length=10)),
                ('apellido2', models.CharField(max_length=10)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoAPP.Categoria')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoAPP.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('nivel_prioridad', models.CharField(max_length=20)),
                ('notas_adicionales_escritas_empleado', models.TextField()),
                ('estado_tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoAPP.Estado')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoAPP.Empleados')),
            ],
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('presupuesto', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoAPP.Clientes')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoAPP.Departamento')),
                ('empleados', models.ManyToManyField(to='ProyectoAPP.Empleados')),
                ('tareas_a_realizar', models.ManyToManyField(to='ProyectoAPP.Tareas')),
            ],
        ),
    ]
