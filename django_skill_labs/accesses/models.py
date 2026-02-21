from django.db import models
from django.utils import timezone


class System(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Sistema"
        verbose_name_plural = "Sistemas"

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name


class Access(models.Model): #dentro de models.py, nome da classe deve sempre ser singular
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="accesses"
    )

    system = models.ForeignKey(
        System,
        on_delete=models.CASCADE,
        related_name="accesses"
    )

    granted_at = models.DateTimeField(auto_now_add=True)

    revoked_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Acesso"
        verbose_name_plural = "Acessos"
        ordering = ['-granted_at'] 
        constraints = [
            models.UniqueConstraint(
                fields=["client", "system"],
                condition=models.Q(revoked_at__isnull=True),
                name="unique_active_access_per_client_system"
            )
        ]

    def revoke(self):
        self.revoked_at = timezone.now()
        self.save()
    
    def __str__(self):
        return f"{self.client} -> {self.system}"