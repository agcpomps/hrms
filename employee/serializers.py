from rest_framework import serializers

from .models import Funcionario, Departamento, Avaliacao, Licenca, DocumentoFuncionario


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = "__all__"


class FuncionarioSerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer()

    class Meta:
        model = Funcionario
        fields = "__all__"


class AvaliacaoSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer()

    class Meta:
        model = Avaliacao
        fields = "__all__"


class LicencaSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer()

    class Meta:
        model = Licenca
        fields = "__all__"


class DocumentoFuncionarioSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer()

    class Meta:
        model = DocumentoFuncionario
        fields = "__all__"
