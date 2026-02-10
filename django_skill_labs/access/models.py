from django.db import models

class System(models.Model):
    id_system = models.AutoField(primary_key=True)
    ''' 
    Campo de identificação do Sistema, sendo este do tipo AutoField
    (inteiro que se auto incrementa) + chave primária
    '''
    
    name_system = models.CharField(max_length=100)
    '''
    Classe que define o nome do Sistema, sendo este do tipo caracter (curto)
    '''

    description_system = models.TextField()
    ''' 
    Campo de texto para a descrição do Sistema. O TextField é usado para armazenar 
    grandes quantidades de texto.
    '''

    def __str__(self):
        return self.name_system
    '''
    Função que retorna o nome do Sistema inserido pelo usuário
    '''

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    '''
    Campo de identificação do cliente, sendo este do tipo AutoField (inteiro que se auto incrementa) 
    e chave primária
    '''

    client_name = models.CharField(max_length=100)
    '''
    Classe que define o nome do cliente, sendo este do tipo caracter (curto)
    '''
    
    client_cpf_cnpj = models.CharField(max_length=20)
    ''' 
    Campo de texto para o CPF ou CNPJ do cliente. O CharField é usado para armazenar
    pequenos textos, como números de identificação.
    '''

    client_email = models.EmailField()
    '''
    Campo de email de contato para o cliente
    '''

    def __str__(self):
        return self.client_name
    '''
    Função que retorna o nome do Cliente inserido pelo usuário
    '''

class Access(models.Model):
    access_id = models.AutoField(primary_key=True)
    '''
    Campo de identificação do Acesso, sendo este do tipo AutoField 
    (inteiro que se auto incrementa) e chave primária
    '''

    access_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    '''
    Chave estrangeira para a função Cliente, com a opção de exclusão em cascata
    '''

    access_system = models.ForeignKey(System, on_delete=models.CASCADE)
    '''
    Chave estrangeira para a função Sistema, com a opção de exclusão em cascata
    '''
    
    access_creation_date = models.DateTimeField(auto_now_add=True)
    '''
    Campo de data e hora para registrar o momento da criação do Acesso, com a opção de 
    adicionar automaticamente a data e hora atual
    '''

    access_date = models.DateTimeField(auto_now_add=True)
    '''
    Campo de data e hora para registrar o momento do acesso, com a opção de adicionar 
    automaticamente a data e hora atual
    '''

    access_log = models.TextField()
    '''
    Campo de texto para registrar o log do acesso
    '''

    def __str__(self):
        return f"Acesso de {self.access_client.client_name} ao sistema {self.access_system.name_system}"
    '''
    # Função que retorna uma string formatada com o nome do cliente e do sistema em que o mesmo está acessando
    '''