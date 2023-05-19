from django.contrib import admin

# Register your models here.
from .models import Departamento, Funcionario, Avaliacao, Licenca, DocumentoFuncionario


admin.site.register(Departamento)
admin.site.register(Funcionario)
