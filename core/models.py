from django.db import models


x = [
        ('pendente','pendente'),
        ('recebido', 'recebido')

        ]


class Lingua(models.Model):
    lingua = models.CharField('Língua', null=False, max_length=50)

    def __str__(self):
        return self.lingua


class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    numero = models.IntegerField('Número de Celular', unique=True)
    senha = models.CharField('Senha',max_length=64)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    nome_pessoa = models.CharField('Nome da Pessoa',null=False, blank=False, max_length=50)
    publicacao = models.CharField('Publicação', max_length=50, null=False)
    quantidade = models.IntegerField('Quantidade', null=False)
    lingua = models.ForeignKey(Lingua, on_delete=models.DO_NOTHING)
    responsavel = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    estado = models.CharField('Estado do pedido',null=False, max_length=10, choices=x, default='pendente')
    especial = models.BooleanField(null=False, default=False)
    data = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.nome_pessoa}: {self.publicacao}'


