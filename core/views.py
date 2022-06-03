from multiprocessing import context
from django.shortcuts import render

from TestDjango.core.form import VehiculoForm
from .models import Vehiculo

# Create your views here.
def home(request):


    return render(request, 'core/home.html')


def home (request):

    contexto={"nombre" : "Yerko Vasquez"}

    return render (request, 'core/home.html', contexto)

def home(request):

    vehiculos = Vehiculo.objects.all()
    datos = {
    'vehiculos' : vehiculos

    }

    return render (request, 'core/home.html', datos)

def form_vehiculo (request):

    datos = {
        'form' : VehiculoForm()
    }

    if request.method == 'POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje' ] = "Guardados correctamente"
    return render (request, 'core/form_vehiculo.html', datos)



def form_mod_vehiculo (request, id):
    Vehiculo = Vehiculo.objects.get(patente= id)

    datos = {
        'form': VehiculoForm(instance=Vehiculo)
    }