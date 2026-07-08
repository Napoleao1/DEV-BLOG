from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
    
    
class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=50, default="Admin")

    conteudo = models.TextField()

    capa = models.ImageField(upload_to='capas/', blank=True, null=True)

    data_publicacao = models.DateTimeField(auto_now_add=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    nome = models.CharField(max_length=100)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return f"Comentário de {self.nome} em {self.artigo.titulo}"


class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.nome}"