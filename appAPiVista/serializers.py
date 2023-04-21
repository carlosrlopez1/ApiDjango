from rest_framework import serializers
from .models import *


class PersonaSeralizer(serializers.ModelSerializer):
    
    class Meta: 
        model = Persona
        fields = '__all__'
        
class FacultadSeralizer(serializers.ModelSerializer):
    
    class Meta: 
        model = Facultad
        fields = '__all__'

class MateriaSeralizer(serializers.ModelSerializer):
    
    class Meta: 
        model = Materia
        fields = '__all__'
        
class Relacion_MateriaSeralizer(serializers.ModelSerializer):
    
    class Meta: 
        model = Relacion_Materia
        fields = '__all__'
                
        

