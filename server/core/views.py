from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response  

from .models import Funcionario, OrdemDeServico, Servicos
from .serializers import FuncionarioSerializer, OrdemDeServicoSerializer

class FuncionarioView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    
    def post(self, request):
        user = request.user
        data = request.data
        funcionario = FuncionarioSerializer(data=data)
        if(funcionario.is_valid()):
            funcionario.save()
            return Response({'message':'ok'}, status=status.HTTP_201_CREATED)
        return Response(funcionario.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    def get(self, request):
        user = request.user
        id = request.GET.get('id')
        if(id):
            funcionario = Funcionario.objects.filter(id=id).first()
            serializer = FuncionarioSerializer(funcionario)
            if(serializer.is_valid()):
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        else:
            funcionario = Funcionario.objects.all()
            serializer = FuncionarioSerializer(funcionario, many=True)
            return Response(serializer.data)
    
    def delete(self, request):
        id = request.data.get('id')
        if(id):
            funcionario = Funcionario.objects.filter(id=id).first()
            funcionario.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)


class OSView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    
    def post(self, request):
        user = request.user
        data = request.data
        os = OrdemDeServicoSerializer(data=data)
        if(os.is_valid()):
            os.save()
            return Response({'message':'ok'}, status=status.HTTP_201_CREATED)
        return Response(os.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    def get(self, request):
        user = request.user
        id = request.GET.get('id')
        if(id):
            os = OrdemDeServico.objects.filter(id=id).first()
            serializer = OrdemDeServicoSerializer(os)
            if(serializer.is_valid()):
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        else:
            os = OrdemDeServico.objects.all()
            serializer = OrdemDeServicoSerializer(os, many=True)
            return Response(serializer.data)
    
    def delete(self, request):
        id = request.data.get('id')
        if(id):
            os = OrdemDeServicoSerializer.objects.filter(id=id).first()
            os.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)

    




    