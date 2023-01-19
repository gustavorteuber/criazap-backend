from django.contrib.auth.models import AbstractUser
from django.db import models
from uploader.models import Image
from django.utils import timezone

class Usuario(AbstractUser):
    recados = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )

class Chats(models.Model):
    texto = models.TextField()
    autor  = models.ForeignKey("core.Usuario",on_delete=models.PROTECT)
    data = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.texto

class Status(models.Model):
    status = models.CharField(max_length=100)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )

    def __str__(self):
        return self.status

class bot(models.Model):
    pergunta = models.CharField(max_length=100)

    def __str__(self):
        return self.pergunta