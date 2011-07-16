# -*- encoding: utf8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from soporte.models import Incidencia
from soporte.forms import CrearIncidenciaForm

@login_required
def dashboard(request):
    print request.user.empleado.nombre_completo
    return render_to_response('soporte/dashboard.html', {
        'user': request.user
    })

@login_required
def mis_incidencias(request):
    incidencias = Incidencia.objects.filter(
       reportada_por=request.user.empleado 
    )
    return render_to_response('soporte/mis_incidencias.html', {
        'user': request.user,
        'incidencias': incidencias
    })

@login_required
def incidencias(request):
    incidencias = Incidencia.objects.all().order_by('-creado_en')
    return render_to_response('soporte/incidencias.html', {
        'user': request.user,
        'incidencias': incidencias
    })

@login_required
def nueva_incidencia(request):
    form = CrearIncidenciaForm()
    if request.method == 'POST':
        form = CrearIncidenciaForm(request.POST)
        if form.is_valid():
            # This decrements the number of books in stock
            # for the requested book
            incidencia = form.save(request)
            return HttpResponseRedirect(reverse('mis_incidencias'))
    return render_to_response(
        'soporte/crear_incidencia.html', 
        {'form': form}
    )
