from django.db import models
from django import forms

# Create your models here.
class Usuario(models.Model):
    IdUsuarios = models.IntegerField()
    IdTipoUsua = models.IntegerField()
    NombUsua = models.CharField(max_length = 50)
    ApellUsua = models.CharField(max_length = 50)
    EmailUsua = models.CharField(max_length = 50)
    PassUsua = forms.CharField(max_length = 50,widget=forms.PasswordInput())
    EstaUsua = models.CharField(max_length = 50)

    def __str__(self):
        return self.NombUsua

