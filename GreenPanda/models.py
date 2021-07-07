from django.db import models

# Create your models here.

class MetodoPago(models.Model):
    idMetodo = models.IntegerField(primary_key=True, verbose_name='Id Metodo')
    Pago = models.CharField(max_length=10, verbose_name='Metodo de Pago')

    def __str__(self):

        return self.Pago

class Proveedor(models.Model):
    numId = models.IntegerField(primary_key=True, verbose_name='Número de Identificación')
    Nombre = models.CharField(max_length=50, verbose_name='Nombre Completo')
    telefono = models.IntegerField(verbose_name='Número de Teléfono')
    Direccion = models.CharField(max_length=50, verbose_name='Dirección')
    Email = models.CharField(max_length=50, verbose_name='Email')
    Pais = models.CharField(max_length=10, verbose_name='Pais')
    Contrasenna = models.CharField(max_length=10, verbose_name='Contraseña')
    Imagen = models.ImageField(null=True, blank=True)
    MetodoPago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)

    def __str__(self):

        return self.Nombre