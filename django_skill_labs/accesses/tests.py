from django.test import TestCase
from django.utils import timezone
from accesses.models import Access, Client, System

class AccessTestCase(TestCase):
    def setUp(self):
        # Cria dados básicos
        self.client_obj = Client.objects.create(name="Empresa Teste")
        self.system_obj = System.objects.create(name="Sistema Teste")

    def test_create_access(self):
        """Criar acesso válido"""
        access = Access.objects.create(client=self.client_obj, system=self.system_obj, granted_at=timezone.now())
        self.assertIsNotNone(access.id)
        self.assertIsNone(access.revoked_at)

    def test_unique_active_constraint(self):
        """Bloqueio de duplicidade"""
        Access.objects.create(client=self.client_obj, system=self.system_obj, granted_at=timezone.now())
        with self.assertRaises(Exception):  # pode ser IntegrityError dependendo do backend
            Access.objects.create(client=self.client_obj, system=self.system_obj, granted_at=timezone.now())

    def test_revoke_access(self):
        """Revogar acesso"""
        access = Access.objects.create(client=self.client_obj, system=self.system_obj, granted_at=timezone.now())
        access.revoked_at = timezone.now()
        access.save()
        self.assertIsNotNone(access.revoked_at)

    def test_create_after_revoke(self):
        """Criar novo acesso após revogação"""
        access1 = Access.objects.create(client=self.client_obj, system=self.system_obj, granted_at=timezone.now())
        access1.revoked_at = timezone.now()
        access1.save()
        access2 = Access.objects.create(client=self.client_obj, system=self.system_obj, granted_at=timezone.now())
        self.assertNotEqual(access1.id, access2.id)
        self.assertIsNone(access2.revoked_at)