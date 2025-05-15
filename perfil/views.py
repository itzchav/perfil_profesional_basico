from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'perfil/index.html')
def publicaciones(request):
    return render(request, 'perfil/publicaciones.html')
def tesis(request):
    return render(request, 'perfil/tesis.html')

