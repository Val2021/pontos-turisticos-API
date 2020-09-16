from rest_framework.viewsets import ModelViewSet
from endereco.models import Enderecos
from .serializers import EnderecoSerializer

class EnderecoViewSet(ModelViewSet):
    queryset = Enderecos.objects.all()
    serializer_class = EnderecoSerializer
