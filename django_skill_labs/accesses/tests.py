'''from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from accesses.models import Access, Client, System
from rest_framework.test import APIClient

class AccessTestCase(TestCase):
    def setUp(self):
        # Cria dados básicos
        self.client_obj = Client.objects.create(name="Empresa Teste")
        self.system_obj = System.objects.create(name="Sistema Teste")
        self.api_client = APIClient()

        # Acessos para testar filtros
        self.access_active = Access.objects.create(client=self.client_obj, system=self.system_obj, granted_at=timezone.now())
        self.access_revoked = Access.objects.create(client=self.client_obj, system=self.system_obj, granted_at=timezone.now(), revoked_at=timezone.now())

        # Autenticação no teste
        self.user = User.objects.create_user(username="test", password="123")
        self.api_client.login(username="test", password="123")

    # --- testes existentes ---
    def test_create_access(self):
        access = Access.objects.create(client=self.client_obj, system=self.system_obj, granted_at=timezone.now())
        self.assertIsNotNone(access.id)
        self.assertIsNone(access.revoked_at)

    def test_unique_active_constraint(self):
        Access.objects.create(client=self.client_obj, system=self.system_obj, granted_at=timezone.now())
        with self.assertRaises(Exception):
            Access.objects.create(client=self.client_obj, system=self.system_obj, granted_at=timezone.now())

    def test_revoke_access(self):
        access = Access.objects.create(client=self.client_obj, system=self.system_obj, granted_at=timezone.now())
        access.revoked_at = timezone.now()
        access.save()
        self.assertIsNotNone(access.revoked_at)

    def test_create_after_revoke(self):
        access1 = Access.objects.create(client=self.client_obj, system=self.system_obj, granted_at=timezone.now())
        access1.revoked_at = timezone.now()
        access1.save()
        access2 = Access.objects.create(client=self.client_obj, system=self.system_obj, granted_at=timezone.now())
        self.assertNotEqual(access1.id, access2.id)
        self.assertIsNone(access2.revoked_at)

    # --- novos testes para /filtered/ ---
    def test_filtered_active_endpoint(self):
        response = self.api_client.get('/api/accesses/filtered/?status=active')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(all(a['revoked_at'] is None for a in data))

    def test_filtered_revoked_endpoint(self):
        response = self.api_client.get('/api/accesses/filtered/?status=revoked')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(all(a['revoked_at'] is not None for a in data))

    def test_filtered_all_endpoint(self):
        response = self.api_client.get('/api/accesses/filtered/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreaterEqual(len(data), 2)  # pelo menos active e revoked
        self.assertTrue(any(a['revoked_at'] is None for a in data))
        self.assertTrue(any(a['revoked_at'] is not None for a in data))'''
