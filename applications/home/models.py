from model_utils.models import TimeStampedModel
from ckeditor.fields import RichTextField

from django.db import models

from applications.users.models import User
from .managers import NewsManager

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
    
class News(TimeStampedModel):
    title = models.CharField("Titulo", max_length=100)
    content = models.TextField("Contenido")
    image = models.ImageField("Imagen", upload_to="articulos/")
    active = models.BooleanField("Activo", default=True)
    breaking_new = models.BooleanField("Ultima noticia")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = NewsManager()


    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.title
    
class Team(TimeStampedModel):
    name = models.CharField('Nombre',max_length=20)
    last_name = models.CharField('Apellido',max_length=20)
    position = models.CharField('Cargo', max_length=30)
    avatar = models.ImageField('Foto', upload_to='team/')

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personales"

    def __str__(self):
        return f"{self.name} {self.last_name}"
    
class Video(TimeStampedModel):
    description = models.CharField('Descripcion', max_length = 120)
    video = models.URLField(("Direccion del Video"))
    active = models.BooleanField("Activo")

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.description

class Publicity(TimeStampedModel):
    title = models.CharField('Titulo', max_length =50)
    description = models.CharField('Descripcion', max_length = 255)
    image = models.ImageField('Baner', upload_to="publicidad/")
    active = models.BooleanField("Activo")

    class Meta:
        verbose_name = "Publicidad"
        verbose_name_plural = "Publicidades"

    def __str__(self):
        return self.title