from django.db import models

class Materias(models.Model):
    nome = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.nome

class Pdf(models.Model):
    nome = models.CharField(max_length=200,default='')
    arquivo = models.FileField(upload_to='pdfs/')
    materia = models.ForeignKey(Materias, related_name='pdfs', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Desafio(models.Model):
    nome = models.CharField(max_length=200, default='')
    arquivo = models.FileField(upload_to='pdfs/')
    materia = models.ForeignKey(Materias, related_name='desafios',on_delete=models.CASCADE )

    def __str__(self):
        return self.nome

