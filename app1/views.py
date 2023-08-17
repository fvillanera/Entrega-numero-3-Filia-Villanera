from django.shortcuts import render
from .models import Curso, Profesor, Estudiante, Fechaproxima
from .forms import CursoForm, Profesorform, Estudianteform
from django.http import HttpResponse

# Create your views here.

def home (request):
    return render(request, "aplicacion/home.html")

def cursos (request):
    contexto = {"cursos": Curso.objects.all(), 'titulo': 'Cursos disponibles', 'comisiones':['comision 1', 'comision 2', 'comision 3']}
    return render(request, "aplicacion/cursos.html", contexto)

def profesores (request):
    contexto = {"profesores": Profesor.objects.all(), 'titulo': 'Profesores disponibles'}
    return render(request, "aplicacion/profesores.html", contexto)

def estudiantes (request):
    contexto = {"estudiantes": Estudiante.objects.all(), 'titulo': 'Estudiantes disponibles'}
    return render(request, "aplicacion/estudiantes.html", contexto)

def fecha_proxima (request):
    contexto = {"fechaproxima": Fechaproxima.objects.all(), 'titulo': 'Proximos cursos y fechas disponibles al'}
    return render(request, "aplicacion/fechaproxima.html", contexto)

def cursoform(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST['nombre'],
                      comision=request.POST['comision'])
        curso.save()
        return HttpResponse("Nueva asignatura/curso agregada con exito!")
    
    return render(request, "aplicacion/cursoform.html")

def cursoform2(request):
    if request.method == "POST":
        miform= CursoForm(request.POST)
        if miform.is_valid():
            name_curso= miform.cleaned_data.get('nombre')
            name_comision= miform.cleaned_data.get('comision')
            curso= Curso(nombre = name_curso,
                         comision= name_comision)
            curso.save()
            return render(request, "aplicacion/base.html")
    else:
        miform= CursoForm()
    return render (request, "aplicacion/cursoform2.html", {"form": miform})


def searchcomision(request):
    return render (request, "aplicacion/searchcomision.html")

def search2(request):
    if request.GET['buscar']:
        patron= request.GET['buscar']
        cursos= Curso.objects.filter(nombre__icontains=patron)
        contexto= {"cursos": cursos, "titulo":f"Busqueda en funcion del caracter '{patron}'"}
        return render(request, "aplicacion/cursos.html", contexto)
    
    return HttpResponse ("Vuelva a intentarlo, ingreso invalido, asegurate de llenar todos los campos")

def profesorform(request):
    if request.method == "POST":
        miform= Profesorform (request.POST)
        if miform.is_valid():
            name_nombre= miform.cleaned_data.get('nombre')
            name_apellido= miform.cleaned_data.get('apellido')
            name_email= miform.cleaned_data.get('email')
            name_profesion= miform.cleaned_data.get('profesion')
            profesor= Profesor(nombre = name_nombre,
                         apellido= name_apellido,
                         email= name_email,
                         profesion= name_profesion)
            profesor.save()
            return render(request, "aplicacion/base.html")
    else:
        miform= Profesorform()
    return render (request, "aplicacion/profesorform.html", {"form": miform})

def searchprofesor(request):
    return render (request, "aplicacion/searchprofesor.html")

def searchprofesor2(request):
    if request.GET['buscar']:
        patron= request.GET['buscar']
        profesores= Profesor.objects.filter(nombre__icontains= patron)
        contexto= {"profesores": profesores}
        return render(request, "aplicacion/profesores.html", contexto)
    
    return HttpResponse ("Vuelva a intentarlo, ingreso invalido, asegurate de llenar todos los campos")


def estudiantesform(request):
    if request.method == "POST":
        miform=  Estudianteform(request.POST)
        if miform.is_valid():
            name_nombre= miform.cleaned_data.get('nombre')
            name_apellido= miform.cleaned_data.get('apellido')
            name_email= miform.cleaned_data.get('email')
            
            estudiante= Estudiante(nombre = name_nombre,
                         apellido= name_apellido,
                         email= name_email,
            )
            estudiante.save()
            return render(request, "aplicacion/base.html")
    else:
        miform= Estudianteform()
    return render (request, "aplicacion/estudianteform.html", {"form": miform})

def searchestudiante(request):
    return render (request, "aplicacion/searchestudiante.html")

def searchestudiante2(request):
    if request.GET['buscar']:
        patron= request.GET['buscar']
        estudiantes= Estudiante.objects.filter(nombre__icontains= patron)
        contexto= {"estudiantes": estudiantes}
        return render(request, "aplicacion/estudiantes.html", contexto)
    
    return HttpResponse ("Vuelva a intentarlo, ingreso invalido, asegurate de llenar todos los campos")