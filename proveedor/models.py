from django.db import models
# class Oficio(models.Model):
#     title = models.CharField(max_length=200)

#     def __str__(self):
#         return self.title

# Create your models here.
class Proveedor(models.Model):
    usuario = models.CharField(max_length=200)
    cedula  = models.CharField(max_length=200)
    nombre  = models.CharField(max_length=200)
    correo  = models.CharField(max_length=200)
    fecha_Nacimiento  = models.CharField(max_length=200)
    celular  = models.CharField(max_length=10)
    años_de_Experiencia  = models.CharField(max_length=2)
    ultimo_Trabajo  = models.CharField(max_length=200)
    costo_Por_Hora  = models.CharField(max_length=10)
    clave  = models.CharField(max_length=200)
    # oficio= models.ForeignKey(Oficio, on_delete=models.CASCADE)

    def __str___(self):
        return self.title