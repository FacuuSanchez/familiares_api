from django.db import models

# Create your models here.
class Persona(models.Model):
    persona = models.CharField(max_length=100)
    documento = models.IntegerField(unique=True)
    fecha_nacimiento = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.persona} - {self.documento}"

class Familiar(models.Model):
    persona = models.ForeignKey(Persona, on_delete= models.CASCADE)
    tipo_vinculo = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
