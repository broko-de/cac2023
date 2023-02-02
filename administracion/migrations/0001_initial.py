# Generated by Django 3.2.14 on 2023-02-02 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('baja', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
                ('fecha_inicio', models.DateField(default=None, null=True, verbose_name='Fecha de inicio')),
                ('portada', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Portada')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='PersonaM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_m', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido_m', models.CharField(max_length=150, verbose_name='Apellido')),
                ('email_m', models.EmailField(max_length=150, null=True)),
                ('dni_m', models.IntegerField(verbose_name='DNI')),
            ],
        ),
        migrations.CreateModel(
            name='DocenteM',
            fields=[
                ('personam_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administracion.personam')),
                ('legajo_m', models.CharField(max_length=10, verbose_name='Legajo')),
            ],
            bases=('administracion.personam',),
        ),
        migrations.CreateModel(
            name='EstudianteM',
            fields=[
                ('personam_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administracion.personam')),
                ('matricula_m', models.CharField(max_length=10, verbose_name='Matricula')),
                ('baja', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Estudiantes',
            },
            bases=('administracion.personam',),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('domicilio', models.CharField(max_length=20, verbose_name='Domicilio')),
                ('foto', models.ImageField(null=True, upload_to='perfiles/', verbose_name='Foto Perfil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('nombre_slug', models.SlugField(max_length=100, verbose_name='Nombre Slug')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
                ('url', models.URLField(max_length=100, verbose_name='Url')),
                ('portada', models.ImageField(null=True, upload_to='imagenes/proyecto/', verbose_name='Portada')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.estudiantem')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(verbose_name='Fecha de creacion')),
                ('estado', models.IntegerField(choices=[(1, 'Inscripto'), (2, 'Cursando'), (3, 'Egresado')], default=1)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.estudiantem')),
            ],
        ),
        migrations.CreateModel(
            name='CursoM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
                ('fecha_inicio', models.DateField(default=None, null=True, verbose_name='Fecha de inicio')),
                ('portada', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Portada')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.categoria')),
                ('estudiantes', models.ManyToManyField(to='administracion.EstudianteM')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='estudiantes',
            field=models.ManyToManyField(through='administracion.Inscripcion', to='administracion.EstudianteM'),
        ),
    ]