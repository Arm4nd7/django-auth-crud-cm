from django.db import models
from django.db.models import  Q

# Create your models here.

##MUEBLES    
class Mueble(models.Model):
    name = models.CharField(max_length=15, null=False)
    MUEBLE_MATERIALS = (
        ('M', 'Madera Sostenible'),
        ('B', 'Bambu'),
        ('E', 'Eco-plasticos'),
        ('C', 'Corcho'),
        ('L', 'Lino Orgonico'),
        ('F', 'Fibras de Coco'),    
    )
    material = models.CharField(max_length=30, null=False, choices=MUEBLE_MATERIALS)
    MUEBLE_STYLES = (
        ('M', 'Minimalista'),
        ('M', 'Multifuncionales'),
        ('S', 'Sostenibles'),
        ('I', 'Industrial'),
    )
    style = models.CharField(max_length=30, null = False, choices = MUEBLE_STYLES)
    cost = models.DecimalField(decimal_places = 4, max_digits = 6, null=False, default=0)
    picture = models.ImageField(upload_to="muebles_images")
    MUEBLE_TYPE = (
        ('O', 'Organizacion'),
        ('H', 'Hool'),
        ('C', 'Confort'),   
    )
    type = models.CharField(max_length=30, null=False, choices=MUEBLE_TYPE)
    
    def __str__(self):
        return self.name

class Cliente(models.Model):
    name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=15, null=False)
    dni = models.IntegerField(null=False, unique=True)
    email = models.EmailField(max_length=50, null=True) 
    #genero
    CLIENTE_GENDER = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    gender = models.CharField(max_length=15, null=False, choices=CLIENTE_GENDER)
    
    def __str__(self):
        return self.name + " " + self.last_name
    
