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
