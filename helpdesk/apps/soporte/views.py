# Create your views here.

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    print request.user.empleado.nombre_completo
    return render_to_response('soporte/dashboard.html', {
        'user': request.user
    })

