from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=12)

def __str__(self) -> str:
    return self.nome

class Maquina(models.Model):
    maquina = models.CharField(max_length=500)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    limpeza = models.IntegerField(default=0)
    concertos = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.maquina
