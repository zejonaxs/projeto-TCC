from django.db import models


class autor(models.Model):

    nome = models.CharField(max_length=150)
    ultimo_nome = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='fotos')

    def __str__(self):
        return self.nome


class orientador(models.Model):

    nome = models.CharField(max_length=150)
    ultimo_nome = models.CharField(max_length=150)
    link_do_curriculo_lattes = models.URLField(max_length=200)

    def __str__(self):
        return self.nome

class curso(models.Model):

    modalidades = (('Bacharelado', 'Bacharelado'), ('Licenciatura', 'Licenciatura'), ('Tecnológo', 'Tecnológo'))

    nome = models.CharField(max_length=150)
    modalidade = models.CharField(max_length=150, choices = modalidades)

    def __str__(self):
        return self.nome


class tcc(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    orientador = models.ForeignKey(orientador, on_delete=models.CASCADE)
    curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    ano_do_documento = models.IntegerField(verbose_name="ano_documento")
    resumo = models.TextField()
    arquivo_do_documento = models.FileField(upload_to='tccs')
    palavras_chave = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

