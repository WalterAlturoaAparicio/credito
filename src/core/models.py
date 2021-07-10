from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
User = get_user_model()

class DeudaSbs(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    monto_deuda = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.monto_deuda)

    def get_sbs_status(self):
        return "{:.2f}".format(self.monto_deuda / 100)

class Solicitud(models.Model):
    SENTINEL_CHOICES = (
        ('B', 'Bueno'),
        ('R', 'Regular'),
        ('M', 'Malo')
    )
    STATUS_CHOICES = (
        ('E', 'En Proceso'),
        ('A', 'Aprovado'),
        ('N', 'No Aprovado')
    )
    user = models.ForeignKey(User, on_delete=CASCADE)
    fecha = models.DateField(auto_now_add=False)
    estado = models.CharField(max_length=1 ,choices=STATUS_CHOICES)
    monto = models.IntegerField(default=0)
    actualizado = models.DateTimeField(auto_now=True)
    sbs_status = models.ForeignKey(DeudaSbs, on_delete=models.CASCADE)
    ia_algoritm = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    sentinel_status = models.CharField(max_length=1, choices=SENTINEL_CHOICES)

    def __str__(self) -> str:
        return self.refernce_number

    def get_monto(self):
        return "{:.2f}".format(self.monto / 100)

    @property 
    def refernce_number(self):
        return f"SOLICITUD-{self.pk}"
