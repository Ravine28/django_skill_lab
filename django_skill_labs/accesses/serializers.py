from rest_framework import serializers
from .models import Access, Client, System


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = '__all__'


class AccessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Access
        fields = '__all__'

    def validate(self, data):
        client = data['client']
        system = data['system']

        already_active = Access.objects.filter(
            client=client,
            system=system,
            revoked_at__isnull=True
        ).exists()

        if already_active:
            raise serializers.ValidationError(
                "Este cliente já possui acesso ativo a este sistema."
            )

        return data