from django.db import models

# Create your models here.
class Pessoa(models.Model): # Classe Mãe
    nome = models.CharField(max_length=100)
    email = models.EmailField() # Email institucional, ex:  lpds1@aluno.ifnmg.edu.br
    senha = models.CharField()
    sexo = models.CharField()
    # Etnia, Renda para gerar informações
    # Curso?

class Aluno(models.Model):
    # Especialização de Pessoa
    cod_matricula = models.CharField()

class Coordenador(models.Model):
    # Especialização de Pessoa
    cod_coordenador = models.CharField()
    data_mandato = models.CharField() # 2022/1 

class CategoriaAc(models.Model):
    # pk = ID
    descricao = models.CharField()
    carga_horaria = models.IntegerField()
    
class AC(models.Model):
    # pk = ID
    categoria = models.ForeignKey(CategoriaAc) # Relacionamento? 1 para 1
    aluno = models.ForeignKey(Aluno) # 1 para N
    coordenador = models.ForeignKey(Coordenador) # 1 para N
    carga_horaria = models.FloatField()
    status = models.CharField() #choices  APROVADO, ANÁLISE, RECUSADO
    comprovante = models.FileField() # Somente PDF