from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    editorial = models.CharField(max_length=30)
    anio = models.DateField(null=True)
    
    
    def __str__(self):
        return f'{self.titulo} es de la editorial {self.editorial}, fue creado el {self.anio}'    


