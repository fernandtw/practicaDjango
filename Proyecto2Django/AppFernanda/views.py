from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hola soy el index</h1>")

def pagina(request):
    return HttpResponse("<h1>Hola la pagina 2</h1>")

# Create your views here.
