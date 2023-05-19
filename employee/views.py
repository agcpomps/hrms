from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Funcionario, Departamento
from .serializers import FuncionarioSerializer, DepartamentoSerializer


class DepartamentoViewSet(viewsets.ViewSet):
    """Retorna todos os Departamentos"""

    queryset = Departamento.objects.all()

    @extend_schema(responses=DepartamentoSerializer)
    def list(self, request):
        serializer = DepartamentoSerializer(self.queryset, many=True)
        return Response(serializer.data)


class FuncionarioViewsSet(viewsets.ViewSet):
    """Retorna todos os funcionários"""
    queryset = Funcionario.objects.all()

    @extend_schema(responses=FuncionarioSerializer)
    def list(self, request):
        serializer = FuncionarioSerializer(self.queryset, many=True)
        return Response(serializer.data)


# Create your views here.
