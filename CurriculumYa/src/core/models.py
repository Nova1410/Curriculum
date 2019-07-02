from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Contacto(models.Model):
    email = models.EmailField(max_length = 50,verbose_name = "Correo electrónico")
    asunto = models.CharField(max_length = 50,default='Asunto',verbose_name = "Asunto")
    msj = RichTextField(max_length = 50,default='Quisiera',verbose_name = "Mensaje")
    
    class Meta:
        verbose_name = "Mensaje contacto"
        verbose_name_plural = "Mensajes de contactos"

    def __str__(self):
        return self.asunto

        