from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('', home, name="home" ),
    path('cursos/', cursos, name="cursos" ),
    path('profesores/', profesores, name="profesores" ),
    path('estudiantes/', estudiantes, name="estudiantes" ),
    path('fechaproxima/', fecha_proxima, name="fechaproxima" ),

    path('curso_form/', cursoform, name="curso_form" ),
    path('curso_form2/', cursoform2, name="curso_form2" ),#agregar guardar curso

    path('buscar_comision/',searchcomision, name="buscar_comision" ),#buscar curso
    path('buscar2/', search2, name="buscar2" ),

    path('profesorform/', profesorform, name="profesorform" ),#agregar/guardar profesor
    path('search_profesor/',searchprofesor, name="search_profesor" ),#buscar profesor
    path('buscar3/', searchprofesor2, name="buscar3" ),

    path('estudianteform/', estudiantesform, name="estudianteform" ),#agregar estudiante
    path('searchestudiante/', searchestudiante, name="searchestudiante" ),
    path('buscar4/', searchestudiante2, name="buscar4" ),
]