from django.db import models

class Sistema(models.Model):
    nome = models.CharField(max_length=100) # Classe que define o nome do sistema, sendo este do tipo caracter (curto)

    def __str__(self):
        return self.nome # Função que retorna o nome do Sistema inserido pelo usuário

class Cliente(models.Model):
    nome = models.CharField(max_length=100) # Classe que define o nome do cliente, sendo este do tipo caracter (curto)

    acesso = models.ManyToManyField(Sistema, blank=True) # ManyToManyField para criar a relação entre Cliente e Sistema. O comando blank=True permite que um cliente possa ser criado sem acesso a nenhum sistema inicialmente.
    def __str__(self):
        return self.nome # Função que retorna o nome do Cliente inserido pelo usuário
