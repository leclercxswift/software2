from django.db import models

# Create your models here.
class Producto(models.Model):
     CATEGORIES = [
        ("Acc","Accion"),
        ("Adv","Aventura"),
        ("Arc","Arcade"),
        ("Dep","Deportes"),
        ("Est","Estrategia"),
        ("Sim","Simulacion"),
        ("Gad","Aventura Grafica"),
        ("Rol","Rol"),
        ("Mus","Musical"),
        ("Box","Sandbox"),
        ("Ter","Terror")
    ]
     title = models.CharField(max_length=50)
     description =models.TextField(max_length=150)
     price = models.FloatField()
     img = models.ImageField(upload_to='productosapp')
     category =models.CharField(max_length=20,choices=CATEGORIES)
     prolink=models.URLField(max_length = 200,default="https://www.epicgames.com/site/es-ES/home?sessionInvalidated=true")
    
     class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"
     def __str__(self):
        return self.title