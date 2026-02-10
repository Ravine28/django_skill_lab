from django.db import models

class System(models.Model):
    system_name = models.CharField(max_length=100)
    '''
    Variável de identificação do Sistema, sendo este do tipo AutoField
    que define o nome do Sistema, sendo este do tipo caracter (curto)
    '''

    system_description  = models.TextField()
    ''' 
    Variável de identificação do Sistema, sendo este do tipo AutoField
    de texto para a descrição do Sistema. O TextField é usado para armazenar 
    grandes quantidades de texto.
    '''

    system_creation_date = models.DateTimeField(auto_now_add=True)
    '''
    Variável de identificação do Sistema, sendo este do tipo AutoField
    de data e hora para registrar o momento da criação do Sistema, com a opção de 
    adicionar automaticamente a data e hora atual
    '''

    def __str__(self):
        return self.system_name
    '''
    Função que retorna o nome do Sistema inserido pelo usuário
    '''

class Client(models.Model):
    lient_name = models.CharField(max_length=100)
    '''
    Variável que recebe o nome do cliente, sendo este do tipo caracter (curto)
    '''
    
    client_cpf_cnpj = models.CharField(max_length=20)
    ''' 
    Variável de texto para o CPF ou CNPJ do cliente. O CharField é usado para armazenar
    pequenos textos, como números de identificação.
    '''

    client_email = models.EmailField()
    '''
    Variável que recebe o email de contato do cliente
    '''

    client_creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name
    '''
    Função que retorna o nome do Cliente inserido pelo usuário
    '''

class Access(models.Model):
    access_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    '''
    Variável de estrangeira para a função Cliente, com a opção de exclusão em cascata
    '''

    access_system = models.ForeignKey(System, on_delete=models.CASCADE)
    '''
    Variável de chave estrangeira para a função Sistema, com a opção de exclusão em cascata
    '''
    
    access_creation_date = models.DateTimeField(auto_now_add=True)
    '''
    Variável que recebe data e hora para registrar o momento da criação do Acesso, com a opção de 
    adicionar automaticamente a data e hora atual
    '''

    access_date = models.DateTimeField(auto_now_add=True)
    '''
    Variável que recebe data e hora para registrar o momento do acesso, com a opção de adicionar 
    automaticamente a data e hora atual
    '''

    access_log = models.TextField()
    '''
    Variável de texto para registrar o log do acesso
    '''

    def __str__(self):
        return f"Acesso de {self.access_client.client_name} ao sistema {self.access_system.system_name}"
    '''
    Função que retorna uma string formatada com o nome do cliente e do sistema em que o mesmo está acessando
    '''