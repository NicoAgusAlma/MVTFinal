# from curses.ascii import HT
import email
import re
import requests
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from AppFinal.models import Usuario, Direccion, Estudio
from AppFinal.forms import UsuarioFormulario, DireccionFormulario, EstudioFormulario

def inicio(request):
    return render(request, 'AppFinal/inicio.html')

def crearDireccion(request):
    return render(request, 'AppFinal/crearDireccion.html')

def buscarDireccion(request):
    return render(request, 'AppFinal/buscarDireccion.html')

def crearEstudio(request):
    return render(request, 'AppFinal/crearEstudio.html')

def buscarEstudio(request):
    return render(request, 'AppFinal/buscarEstudio.html')

def datosGuardados(request):
    return render(request, 'AppFinal/datosGuardados.html')

def usuario(self):
    usuario = Usuario(nombre='NombrePython', apellido='ApellidoPython', mail='mailpytho@gmail.com', password='2222333', nacimiento='1932-05-25')
    usuario.save()
    documentoDeTexto = f'--->Usuario: {usuario.nombre}   Apellido:{usuario.apellido}    mail:{usuario.mail}    contraseña:{usuario.password}    nacimiento:{usuario.nacimiento}'

    return HttpResponse(documentoDeTexto)

def crearUsuario(request):

    if request.method == 'POST':
        miFormulario = UsuarioFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            usuario = Usuario(nombre=informacion['nombre'], apellido=informacion['apellido'], mail=informacion['mail'], password=informacion['password'], nacimiento=informacion['nacimiento'])

            usuario.save()

            return render(request, 'AppFinal/datosGuardados.html')

    else:

        miFormulario = UsuarioFormulario()

    return render(request, 'AppFinal/crearUsuario.html', {"miFormulario":miFormulario})

def buscarUsuario(request):

    return render(request, 'AppFinal/buscarUsuario.html')

def buscarU(request):
    if request.GET['nombre']:

        nombre=request.GET['nombre']
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
        
        return render(request, 'AppFinal/buscarUsuario.html', {'usuarios': usuarios, 'nombre': nombre})
    
    else:

        respuesta = 'No enviaste datos' 

        return render(request, 'AppFinal/buscarUsuario.html', {'respuesta':respuesta})

def crearDireccion(request):

    if request.method == 'POST':
        miFormulario2 = DireccionFormulario(request.POST)
        print(miFormulario2)

        if miFormulario2.is_valid:
            informacion = miFormulario2.cleaned_data

            direccion = Direccion(pais=informacion['pais'], provincia=informacion['provincia'], localidad=informacion['localidad'], calle=informacion['calle'], numero=informacion['numero'])

            direccion.save()

            return render(request, 'AppFinal/datosGuardados.html')

    else:

        miFormulario2 = DireccionFormulario()

    return render(request, 'AppFinal/crearDireccion.html', {"miFormulario2":miFormulario2})

def buscarDireccion(request):

    return render(request, 'AppFinal/buscarDireccion.html')

def buscarD(request):
    if request.GET['calle']:

        calle=request.GET['calle']
        direcciones = Direccion.objects.filter(calle__icontains=calle)
        return render(request, 'AppFinal/buscarDireccion.html', {'direcciones': direcciones, 'calle': calle})
    
    else:

        respuesta = 'No enviaste datos' 

        return render(request, 'AppFinal/buscarDireccion.html', {'respuesta':respuesta})
    

def crearEstudio(request):

    if request.method == 'POST':
        miFormulario3 = EstudioFormulario(request.POST)
        print(miFormulario3)

        if miFormulario3.is_valid:
            informacion = miFormulario3.cleaned_data

            institucion = Estudio(institucion=informacion['institucion'], carrera=informacion['carrera'], tiempoCursado=informacion['tiempoCursado'], egresado=informacion['egresado'])

            institucion.save()

            return render(request, 'AppFinal/datosGuardados.html')

    else:

        miFormulario3 = EstudioFormulario()

    return render(request, 'AppFinal/crearEstudio.html', {"miFormulario3":miFormulario3})

def buscarEstudio(request):

    return render(request, 'AppFinal/buscarEstudio.html')

def buscarE(request):
    if request.GET['busqueda']:
        search_param = request.GET['busqueda']
        print(search_param)
        query = Q(institucion__contains=search_param)
        query.add(Q(carrera__contains=search_param), Q.OR)
        query.add(Q(tiempoCursado__contains=search_param), Q.OR)
        query.add(Q(egresado__contains=search_param), Q.OR)
        estudios = Estudio.objects.filter(query)
        context_dict = {
            'estudios': estudios
        }
        
        return render(
            request=request,
            context=context_dict,
            template_name="AppFinal/buscarEstudio.html",
        )
    else:

        respuesta = 'No ingresó ningun dato' 

        return render(request, 'AppFinal/buscarEstudio.html', {'respuesta':respuesta})
    




    # if request.GET['institucion']:

    #     institucion=request.GET['institucion']
    #     estudios = Estudio.objects.filter(institucion__icontains=institucion)
        
    #     return render(request, 'AppFinal/buscarEstudio.html', {'estudios': estudios, 'institucion': institucion})
    
    # else:

    #     respuesta = 'No enviaste datos' 

    #     return render(request, 'AppFinal/buscarEstudio.html', {'respuesta':respuesta})# from curses.ascii import HT
import email
import re
import requests
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from AppFinal.models import Usuario, Direccion, Estudio
from AppFinal.forms import UsuarioFormulario, DireccionFormulario, EstudioFormulario

def inicio(request):
    return render(request, 'AppFinal/inicio.html')

def crearDireccion(request):
    return render(request, 'AppFinal/crearDireccion.html')

def buscarDireccion(request):
    return render(request, 'AppFinal/buscarDireccion.html')

def crearEstudio(request):
    return render(request, 'AppFinal/crearEstudio.html')

def buscarEstudio(request):
    return render(request, 'AppFinal/buscarEstudio.html')

def datosGuardados(request):
    return render(request, 'AppFinal/datosGuardados.html')

def usuario(self):
    usuario = Usuario(nombre='NombrePython', apellido='ApellidoPython', mail='mailpytho@gmail.com', password='2222333', nacimiento='1932-05-25')
    usuario.save()
    documentoDeTexto = f'--->Usuario: {usuario.nombre}   Apellido:{usuario.apellido}    mail:{usuario.mail}    contraseña:{usuario.password}    nacimiento:{usuario.nacimiento}'

    return HttpResponse(documentoDeTexto)

def crearUsuario(request):

    if request.method == 'POST':
        miFormulario = UsuarioFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            usuario = Usuario(nombre=informacion['nombre'], apellido=informacion['apellido'], mail=informacion['mail'], password=informacion['password'], nacimiento=informacion['nacimiento'])

            usuario.save()

            return render(request, 'AppFinal/datosGuardados.html')

    else:

        miFormulario = UsuarioFormulario()

    return render(request, 'AppFinal/crearUsuario.html', {"miFormulario":miFormulario})

def buscarUsuario(request):

    return render(request, 'AppFinal/buscarUsuario.html')

def buscarU(request):
    if request.GET['nombre']:

        nombre=request.GET['nombre']
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
        
        return render(request, 'AppFinal/buscarUsuario.html', {'usuarios': usuarios, 'nombre': nombre})
    
    else:

        respuesta = 'No enviaste datos' 

        return render(request, 'AppFinal/buscarUsuario.html', {'respuesta':respuesta})

def crearDireccion(request):

    if request.method == 'POST':
        miFormulario2 = DireccionFormulario(request.POST)
        print(miFormulario2)

        if miFormulario2.is_valid:
            informacion = miFormulario2.cleaned_data

            direccion = Direccion(pais=informacion['pais'], provincia=informacion['provincia'], localidad=informacion['localidad'], calle=informacion['calle'], numero=informacion['numero'])

            direccion.save()

            return render(request, 'AppFinal/datosGuardados.html')

    else:

        miFormulario2 = DireccionFormulario()

    return render(request, 'AppFinal/crearDireccion.html', {"miFormulario2":miFormulario2})

def buscarDireccion(request):

    return render(request, 'AppFinal/buscarDireccion.html')

def buscarD(request):
    if request.GET['calle']:

        calle=request.GET['calle']
        direcciones = Direccion.objects.filter(calle__icontains=calle)
        return render(request, 'AppFinal/buscarDireccion.html', {'direcciones': direcciones, 'calle': calle})
    
    else:

        respuesta = 'No enviaste datos' 

        return render(request, 'AppFinal/buscarDireccion.html', {'respuesta':respuesta})
    

def crearEstudio(request):

    if request.method == 'POST':
        miFormulario3 = EstudioFormulario(request.POST)
        print(miFormulario3)

        if miFormulario3.is_valid:
            informacion = miFormulario3.cleaned_data

            institucion = Estudio(institucion=informacion['institucion'], carrera=informacion['carrera'], tiempoCursado=informacion['tiempoCursado'], egresado=informacion['egresado'])

            institucion.save()

            return render(request, 'AppFinal/datosGuardados.html')

    else:

        miFormulario3 = EstudioFormulario()

    return render(request, 'AppFinal/crearEstudio.html', {"miFormulario3":miFormulario3})

def buscarEstudio(request):

    return render(request, 'AppFinal/buscarEstudio.html')

def buscarE(request):
    if request.GET['busqueda']:
        search_param = request.GET['busqueda']
        print(search_param)
        query = Q(institucion__contains=search_param)
        query.add(Q(carrera__contains=search_param), Q.OR)
        query.add(Q(tiempoCursado__contains=search_param), Q.OR)
        query.add(Q(egresado__contains=search_param), Q.OR)
        estudios = Estudio.objects.filter(query)
        context_dict = {
            'estudios': estudios
        }
        
        return render(
            request=request,
            context=context_dict,
            template_name="AppFinal/buscarEstudio.html",
        )
    else:

        respuesta = 'No ingresó ningun dato' 

        return render(request, 'AppFinal/buscarEstudio.html', {'respuesta':respuesta})
    




    # if request.GET['institucion']:

    #     institucion=request.GET['institucion']
    #     estudios = Estudio.objects.filter(institucion__icontains=institucion)
        
    #     return render(request, 'AppFinal/buscarEstudio.html', {'estudios': estudios, 'institucion': institucion})
    
    # else:

    #     respuesta = 'No enviaste datos' 

    #     return render(request, 'AppFinal/buscarEstudio.html', {'respuesta':respuesta})