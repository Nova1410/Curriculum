from django.shortcuts import render
from .models import Experiencia
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.


class ExperienciaCreation(CreateView):
    model = Experiencia
    success_url = reverse_lazy('perfil:inicio')
    fields = ['IdUsuarios','NombHabil','NiveHabil']



def perfil(request):
    return render(request,'perfil.html')



