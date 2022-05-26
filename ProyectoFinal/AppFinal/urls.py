from xml.etree.ElementInclude import include
from django.urls import path
from AppFinal import views
import AppFinal


urlpatterns = [
    path('', views.inicio, name='Home'),
    path('crearUsuario', views.crearUsuario, name= 'CrearUsuario'),
    path('buscarUsuario', views.buscarUsuario, name= 'BuscarUsuario'),
    path('crearDireccion', views.crearDireccion, name= 'CrearDireccion'),
    path('buscarDireccion', views.buscarDireccion, name= 'BuscarDireccion'),
    path('crearEstudios', views.crearEstudio, name= 'CrearEstudio'),
    path('buscarEstudios', views.buscarEstudio, name= 'BuscarEstudio'),
    path('datosGuardados', views.datosGuardados, name= 'DatosGuardados'),
    # path('resultadoBusqueda', views.resultadoBusqueda , name= 'resultadoBusqueda'),
    path('usuario', views.usuario, name= 'usuario'),
    path('buscarU/', views.buscarU),
    path('buscarD/', views.buscarD),
    path('buscarE/', views.buscarE),
]
