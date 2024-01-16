from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='avatar/', null=True)
    
    
    def __str__(self):
        return self.nome

class Servicos(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class OrdemDeServico(models.Model):
    cliente = models.CharField(max_length=255)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50)
    funcionarios = models.ManyToManyField(Funcionario, related_name='funcionarios_os')
    servicos = models.ManyToManyField(Servicos, related_name='servicos_os')
    

    def __str__(self):
        return f"Ordem de Serviço {self.id} - {self.cliente}"

class Fotos(models.Model):
    ordem_de_servico = models.ForeignKey(OrdemDeServico, related_name='fotos', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='ordens_servicos/')
    descricao = models.CharField(max_length=255, blank=True)
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foto {self.id} - Ordem de Serviço {self.ordem_de_servico.id}"


