from rest_framework import serializers

from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        #não pricsa colocar todos os campos
        fields = ['id', 'nome', 'endereco', 'idade']