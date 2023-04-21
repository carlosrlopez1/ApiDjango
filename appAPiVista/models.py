from django.db import models

# Create your models here.
class Facultad(models.Model):
   

    # Campos
    nombre = models.CharField(max_length=50,blank=False,null=False,unique=True)

    # Metadata
    class Meta:
        ordering = ["nombre"]
        verbose_name =('facultad')
        verbose_name_plural =('facultades')
   
    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.nombre
    
class Persona(models.Model):
   

    # Campos
    nombre = models.CharField(max_length=50,blank=False,null=False)
    apellido = models.CharField(max_length=50,blank=False,null=False)
    foto = models.FileField(upload_to='media',blank=False,null=False,max_length=100)
    identificacion = models.BigIntegerField(blank=False,null=False,unique=True,primary_key=True)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)   
    facultad = models.ForeignKey(Facultad,on_delete=models.SET_NULL,null=True)
    # Metadata
    class Meta:
        ordering = ["nombre"]
        verbose_name =('Persona')
        verbose_name_plural =('Personas')
   
    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.nombre
    
class Materia(models.Model):
   

    # Campos
    nombre = models.CharField(max_length=50,blank=False,null=False)
    N_credito = models.PositiveIntegerField(blank=False,null=False)
       
    # Metadata
    class Meta:
        ordering = ["nombre"]
        verbose_name =('Materia')
        verbose_name_plural =('Materias')
   
    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.nombre
    
class Relacion_Materia(models.Model):
   
    # Campos
    id = models.BigAutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona,on_delete=models.SET_NULL,null=True)
    id_materia = models.ForeignKey(Materia,on_delete=models.SET_NULL,null=True)
        
    # Metadata
    class Meta:
        ordering = ["id"]
        verbose_name =('Relacion_Materia')
        verbose_name_plural =('Relacion_Materias')
   
    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return str(self.id_persona.nombre + " " + str(self.id_materia.nombre)) 
