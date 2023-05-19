from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Departamento(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=True, null=True)
    cargo = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.CharField(max_length=255)
    formacao = models.CharField(max_length=255)
    numero_de_agente = models.IntegerField()
    nif = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    data_de_entrada = models.DateField()
    departamento = models.ForeignKey(
        Departamento, on_delete=models.CASCADE, related_name='funcionarios')
    activo = models.BooleanField(default=True)

    def anos_de_trabalho(self):
        hoje = timezone.now().date()
        anos = hoje.year - self.data_de_entrada.year
        if hoje.month < self.data_de_entrada.month or (hoje.month == self.data_de_entrada.month and hoje.day < self.data_de_entrada.day):
            anos -= 1
        return anos

    def __str__(self) -> str:
        return self.nome


class Avaliacao(models.Model):
    data = models.DateField()
    nota = models.FloatField()
    comentario = models.TextField(blank=True, null=True)
    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.CASCADE, related_name="avaliacoes")

    def __str__(self) -> str:
        return f"Avaliação de {self.funcionario.nome} - Nota: {self.nota}"


class TipoLicenca(models.TextChoices):
    MEDICA = 'medica', _('Licença médica')
    FERIAS = 'ferias', _('Férias')
    MATERNIDADE = 'maternidade', _('Licença maternidade')
    PATERNIDADE = 'paternidae', _('Licença paternidade')


class Licenca(models.Model):
    tipo = models.CharField(
        max_length=20,
        choices=TipoLicenca.choices,
        default=TipoLicenca.MEDICA
    )

    inicio = models.DateField()
    fim = models.DateField()
    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.CASCADE,
        related_name='licencas'
    )


class DocumentoFuncionario(models.Model):
    nome = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to='documentos/funcionarios')
    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.CASCADE, related_name='documentos_funcionario')

    def __str__(self) -> str:
        return self.nome
