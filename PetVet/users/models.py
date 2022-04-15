from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=50, null=True,
                            verbose_name='Nome Completo')
    cpf = models.CharField(max_length=14, null=True,
                           verbose_name='CPF')
    phone = models.CharField(max_length=16, null=True,
                             verbose_name='Telefone')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
