from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=150)
    edad = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'persona'
        verbose_name = 'personas'
        db_table = 'personas'