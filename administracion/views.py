from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, redirect

from django.template import loader

from administracion.forms import CategoriaForm, CursoForm, CategoriaFormValidado, EstudianteForm,ProyectoForm,RegistrarUsuarioForm

from administracion.models import Categoria, Curso, Estudiante, Proyecto

from django.contrib import messages


from django.views.generic import ListView
from django.views import View

from django.conf import settings

from  django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
"""
    Vistas de la parte administracion
"""
@login_required(login_url=settings.LOGIN_URL)
def index_administracion(request):
    #EJEMPLO DE CONSULTA SI UN USUARIO PERTENECE A UN GRUPO
    if not request.user.groups.filter(name="administracion").exists():
        return render(request,'administracion/403_admin.html')
    variable = 'test variable'
    return render(request,'administracion/index_administracion.html',{'variable':variable})

"""
    CRUD Categorias
"""
@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.view_categoria', login_url=settings.LOGIN_URL)
def categorias_index(request):
    #queryset
    categorias = Categoria.objects.filter(baja=False)
    return render(request,'administracion/categorias/index.html',{'categorias':categorias})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.add_categoria', login_url=settings.LOGIN_URL)
def categorias_nuevo(request):
    if(request.method=='POST'):
        formulario = CategoriaFormValidado(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaFormValidado()
    return render(request,'administracion/categorias/nuevo.html',{'formulario':formulario})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.change_categoria', login_url=settings.LOGIN_URL)
def categorias_editar(request,id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = CategoriaFormValidado(request.POST,instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaFormValidado(instance=categoria)
    return render(request,'administracion/categorias/editar.html',{'formulario':formulario})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.delete_categoria', login_url=settings.LOGIN_URL)
def categorias_eliminar(request,id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    categoria.soft_delete()
    return redirect('categorias_index')

"""
    CRUD Cursos
"""
@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.view_curso', raise_exception=True) #envia una exception 403
def cursos_index(request):
    cursos = Curso.objects.all()
    return render(request,'administracion/cursos/index.html',{'cursos':cursos})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.add_curso', login_url=settings.LOGIN_URL)
def cursos_nuevo(request):
    #forma de resumida de instanciar un formulario basado en model con los
    #datos recibidos por POST si la petición es por POST o bien vacio(None)
    #Si la petición es por GET
    formulario = CursoForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el curso correctamente')          
        return redirect('cursos_index')
    return render(request,'administracion/cursos/nuevo.html',{'formulario':formulario})


@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.change_curso',  raise_exception=True)
def cursos_editar(request,id_curso):
    try:
        curso = Curso.objects.get(pk=id_curso)
    except Curso.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    formulario = CursoForm(request.POST or None,request.FILES or None,instance=curso)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha editado el curso correctamente')          
        return redirect('cursos_index')
    return render(request,'administracion/cursos/editar.html',{'formulario':formulario})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.delete_curso', login_url=settings.LOGIN_URL)
def cursos_eliminar(request,id_curso):
    try:
        curso = Curso.objects.get(pk=id_curso)
    except Curso.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    messages.success(request,'Se ha eliminado el curso correctamente')          
    curso.delete()
    return redirect('cursos_index')

"""
    CRUD Estudiantes
"""
@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.view_estudiantem', login_url=settings.LOGIN_URL)
def estudiantes_index(request):
    estudiantes = Estudiante.objects.all()
    return render(request,'administracion/estudiantes/index.html',{'estudiantes':estudiantes})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.add_estudiantem', login_url=settings.LOGIN_URL)
def estudiantes_nuevo(request):
    formulario = EstudianteForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado al estudiante correctamente')          
        return redirect('estudiantes_index')
    return render(request,'administracion/estudiantes/nuevo.html',{'formulario':formulario})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.change_estudiantem', login_url=settings.LOGIN_URL)
def estudiantes_editar(request,id_estudiante):
    try:
        estudiante = Estudiante.objects.get(pk=id_estudiante)
    except Estudiante.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    formulario = EstudianteForm(request.POST or None,request.FILES or None,instance=estudiante)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha editado al estudiante correctamente')          
        return redirect('estudiantes_index')
    return render(request,'administracion/estudiantes/editar.html',{'formulario':formulario})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.delete_estudiantem', login_url=settings.LOGIN_URL)
def estudiantes_eliminar(request,id_estudiante):
    try:
        estudiante = Proyecto.objects.get(pk=id_estudiante)
    except Proyecto.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    estudiante.delete()
    messages.success(request,'Se ha eliminado al estudiante correctamente')          
    return redirect('proyectos_index')

"""
    CRUD Proyectos
"""
@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.view_proyecto', login_url=settings.LOGIN_URL)
def proyectos_index(request):
    proyectos = Proyecto.objects.all()
    return render(request,'administracion/proyectos/index.html',{'proyectos':proyectos})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.add_proyecto', login_url=settings.LOGIN_URL)
def proyectos_nuevo(request):
    formulario = ProyectoForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el proyecto correctamente')          
        return redirect('proyectos_index')
    return render(request,'administracion/proyectos/nuevo.html',{'formulario':formulario})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.change_proyecto', login_url=settings.LOGIN_URL)
def proyectos_editar(request,id_proyecto):
    try:
        proyecto = Proyecto.objects.get(pk=id_proyecto)
    except Proyecto.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    formulario = ProyectoForm(request.POST or None,request.FILES or None,instance=proyecto)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha editado el proyecto correctamente')          
        return redirect('proyectos_index')
    return render(request,'administracion/proyectos/editar.html',{'formulario':formulario})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.delete_proyecto', login_url=settings.LOGIN_URL)
def proyectos_eliminar(request,id_proyecto):
    try:
        proyecto = Proyecto.objects.get(pk=id_proyecto)
    except Proyecto.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    messages.success(request,'Se ha eliminado el proyecto correctamente')          
    proyecto.delete()
    return redirect('proyectos_index')
    
class CategoriaListView(ListView):
    model = Categoria
    context_object_name = 'lista_categorias'
    template_name= 'administracion/categorias/index.html'
    queryset= Categoria.objects.filter(baja=False)
    ordering = ['nombre']

class CategoriaView(View):
    form_class = CategoriaForm
    template_name = 'administracion/categorias/nuevo.html'

    def get(self, request,*args, **kwargs):
        form = self.form_class()
        return render(request,self.template_name,{'formulario':form})
    
    def post(self,request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias_index')
        return render(request,self.template_name,{'formulario':form})

"""
AUTENTICACION
"""
def cac_login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            nxt = request.GET.get("next",None)
            messages.success(request, f' Bienvenido/a {username} !!')
            if nxt is None:
                return redirect('inicio')
            else:
                return redirect(nxt)
        else:
            messages.error(request, f'Cuenta o password incorrecto, realice el login correctamente')
    form = AuthenticationForm()
    return render(request, 'publica/login.html', {'form': form})

def cac_registrarse(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'publica/registrarse.html', {'form': form})