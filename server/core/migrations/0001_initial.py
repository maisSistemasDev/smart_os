# Generated by Django 4.2.7 on 2024-01-15 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cargo', models.CharField(max_length=255)),
                ('imagem', models.ImageField(null=True, upload_to='avatar/')),
            ],
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrdemDeServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=50)),
                ('funcionarios', models.ManyToManyField(related_name='funcionarios_os', to='core.funcionario')),
                ('servicos', models.ManyToManyField(related_name='servicos_os', to='core.servicos')),
            ],
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='ordens_servicos/')),
                ('descricao', models.CharField(blank=True, max_length=255)),
                ('data_upload', models.DateTimeField(auto_now_add=True)),
                ('ordem_de_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='core.ordemdeservico')),
            ],
        ),
    ]
