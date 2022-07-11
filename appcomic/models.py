from django.db import models

class Comic(models.Model):
    titulo = models.CharField(max_length=30)
    editorial = models.CharField(max_length=30)
    anio = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.titulo} - Editorial {self.editorial} - {self.anio}' 