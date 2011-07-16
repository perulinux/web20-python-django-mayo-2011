# Create your views here.

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from soporte.models import Incidencia

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
