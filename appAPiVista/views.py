from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class FacultadViewSet (viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSeralizer
    
    
class PersonaViewSet (viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSeralizer

class MateriaViewSet (viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSeralizer
    
class Relacion_MateriaViewSet (viewsets.ModelViewSet):
    queryset = Relacion_Materia.objects.all()
    serializer_class = Relacion_MateriaSeralizer
    
