from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('pagina/',views.pagina),
]

