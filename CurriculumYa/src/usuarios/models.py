from django.db import models
from django.contrib.auth.models import User
from src.parametros.models import TipoDocu
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Perfil(models.Model):
    #El usuario al cual pertenece el perfil
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name = "Usuario")
    #Datos adicionales que queramos que tenga el usuario
    IdUsuarios = models.CharField(max_length = 11,verbose_name = "Id usuario",primary_key=True)
    Titulo = models.CharField(max_length = 100, default = "", verbose_name = "Título")
    Ocup = models.CharField(max_length = 100, default = "", verbose_name = "Ocupación")

    class Meta():
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return str(self.IdUsuarios)
    

    # #Señales
    # @receiver(post_save, sender=User)
    # def create_user_perfil(sender, instance, created, **kwargs):
    #     if created:
    #         Perfil.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_perfil(sender, instance, **kwargs):
    #     instance.perfil.save()
