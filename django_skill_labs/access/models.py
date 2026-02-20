from django.db import models

class System(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Access(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="accesses")
    system = models.ForeignKey(System, on_delete=models.CASCADE, related_name="accesses")
    created_at = models.DateTimeField(auto_now_add=True) 
    is_active = models.BooleanField(default=True) #campo para REVOKE

    def __str__(self):
        return f"Acesso: {self.client.name} ao {self.system.name}"