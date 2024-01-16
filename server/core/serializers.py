from rest_framework import serializers
from .models import Funcionario, OrdemDeServico

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__' 

class OrdemDeServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemDeServico
        fields = '__all__'

