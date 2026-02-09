from django.db import models

class Sistema(models.Model):
    id_sistema = models.AutoField(primary_key=True) # Campo de identificação do sistema, sendo este do tipo AutoField (inteiro que se auto incrementa) e chave primária
    nome_sistema = models.CharField(max_length=100) # Classe que define o nome do sistema, sendo este do tipo caracter (curto)
    descricao_sistema = models.TextField() # Campo de texto para a descrição do sistema
    def __str__(self):
        return self.nome_sistema # Função que retorna o nome do Sistema inserido pelo usuário
    
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True) # Campo de identificação do cliente, sendo este do tipo AutoField (inteiro que se auto incrementa) e chave primária
    nome_cliente = models.CharField(max_length=100) # Classe que define o nome do cliente, sendo este do tipo caracter (curto)
    cpf_cnpj_cliente = models.CharField(max_length=20) # Campo de texto para o CPF ou CNPJ do cliente
    email_cliente = models.EmailField() # Campo de email para o cliente
    def __str__(self):
        return self.nome_cliente # Função que retorna o nome do Cliente inserido pelo usuário

class Acesso(models.Model):
    id_acesso = models.AutoField(primary_key=True) # Campo de identificação do acesso, sendo este do tipo AutoField (inteiro que se auto incrementa) e chave primária
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) # Chave estrangeira para o cliente, com a opção de exclusão em cascata
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE) # Chave estrangeira para o sistema, com a opção de exclusão em cascata
    data_criacao_acesso = models.DateTimeField(auto_now_add=True) # Campo de data e hora para registrar o momento da criação do acesso, com a opção de adicionar automaticamente a data e hora atual
    data_acesso = models.DateTimeField(auto_now_add=True) # Campo de data e hora para registrar o momento do acesso, com a opção de adicionar automaticamente a data e hora atual
    log_acesso = models.TextField() # Campo de texto para registrar o log do acesso
    def __str__(self):
        return f"Acesso de {self.cliente.nome_cliente} ao sistema {self.sistema.nome_sistema}" # Função que retorna uma string formatada com o nome do cliente e do sistema para identificar o acesso