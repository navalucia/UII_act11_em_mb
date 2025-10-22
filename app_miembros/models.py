from django.db import models

class Membresia(models.Model):
    id_membresia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo_mensual = models.DecimalField(max_digits=8, decimal_places=2)
    acceso_limitado = models.BooleanField(default=False)
    acceso_entrenador = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - ${self.costo_mensual}"


class Miembro(models.Model):
    id_miembro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    fecha_registro = models.DateField(auto_now_add=True)
    membresia = models.ForeignKey(Membresia, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"