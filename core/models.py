from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from endereco.models import Enderecos


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracoes)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    enderecos = models.ForeignKey(
        Enderecos, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.nome
