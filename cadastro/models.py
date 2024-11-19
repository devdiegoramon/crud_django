from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome