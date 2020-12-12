from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')
def operaciones(request):
    return render(request,'Operaciones.html')
def trcuentapropia(request):
    return render(request,'trcuentaspropias.html')

def trcuentaterceros(request):
    return render(request,'trcuentasterceros.html')
def preautorizacion(request):
    return render(request,'preautorizacion.html')
def pagoplanilla(request):
    return render(request,'pagoplanilla.html')