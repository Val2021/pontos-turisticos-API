from rest_framework.serializers import ModelSerializer
from endereco.models import Enderecos

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Enderecos
        fields = [
            'linha1', 'linha2','cidade','estado','pais',
            'latitude','longitude']