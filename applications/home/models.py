from model_utils.models import TimeStampedModel
from ckeditor.fields import RichTextField

from django.db import models


# Create your models here.

class Home(TimeStampedModel):
    title =  models.CharField("Titulo", max_length=100)
    content = models.TextField("Contenido")
    image = models.ImageField("Imagen", upload_to="home/")
    background_image = models.ImageField("imagen de Fondo", upload_to="home/")
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Portada"
        verbose_name_plural = "Portadas"

    def __str__(self):
        return self.title
    
class Articles(TimeStampedModel):
    title = models.CharField("Titulo", max_length=100)
    content = models.TextField("Contenido")
    image = models.ImageField("Imagen", upload_to="articulos/")
    active = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self):
        return self.title