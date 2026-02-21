from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Access, Client, System
from .serializers import AccessSerializer, ClientSerializer, SystemSerializer


class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer

    @action(detail=True, methods=['post'])
    def revoke(self, request, pk=None):
        accesses = self.get_object()

        if accesses.revoked_at:
            return Response({"detail": "Acesso já revogado."})

        accesses.revoke()

        return Response({"detail": "Acesso revogado com sucesso."})


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer