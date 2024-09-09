from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Soy el index del Inicio 1 Hola</h1>")


def index2(request):
    return HttpResponse("<h1>Soy el index del Inicio 2 Adios</h1>")
