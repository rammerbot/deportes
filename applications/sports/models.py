from model_utils.models import TimeStampedModel
from ckeditor.fields import RichTextField

from django.db import models

# Create your models here.

# Registro de deportes
class Sports(TimeStampedModel):
    sport = models.CharField('Deporte',max_length=100)
    description = RichTextField('Descripcion')
    image = models.ImageField('Imagen', upload_to='deportes/')

    class Meta:
        verbose_name = "Deporte"
        verbose_name_plural = "Deportes"
    
    def __str__(self):
        return self.sport

# Categorias deportivas
class SportCategories(TimeStampedModel):
    category = models.CharField("Categoria", max_length=100)
    sport = models.ForeignKey(Sports, on_delete=models.CASCADE)
    description = RichTextField('Descripcion')
    image = models.ImageField("Imagen", upload_to='Categoria_deportiva')

    class Meta:
        verbose_name = "Categoria Deportiva"
        verbose_name_plural = "Categorias Deportivas"

    def __str__(self) -> str:
        return self.category

# Equipos
class Teams(TimeStampedModel):
    name = models.CharField("Nombre", max_length=50)
    image = models.ImageField('Imagen', upload_to='Equipos/')
    sport_category = models.ForeignKey(SportCategories, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        
    def __str__(self):
        return self.name

# Eventos proximos
class Events(TimeStampedModel):
    event = models.CharField('Evento', max_length=100)
    sport = models.ForeignKey(Sports, on_delete=models.CASCADE)
    sport_category = models.ForeignKey(SportCategories, on_delete=models.CASCADE)
    description = models.TextField("descripcion")
    home_team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='home_event')
    visitor_team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='visitor_event')
    date = models.DateTimeField('Fecha')
    

    @property
    def home_image(self):
        return self.home_team.image.url if self.home_team else None

    @property
    def visitor_image(self):
        return self.visitor_team.image.url if self.visitor_team else None
    
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.event

# Resultado de eventos 
class Result(TimeStampedModel):
    event_name = models.CharField('Final de Evento', max_length=100)
    sport_category = models.ForeignKey(SportCategories, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    visitor_team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='visitor_result')
    home_goals = models.PositiveIntegerField('Marcador del Local')
    visitors_goals = models.PositiveIntegerField('Marcador del visitante')
    date = models.DateTimeField('Fecha')

    @property
    def home_image(self):
        return self.home_team.image.url if self.home_team else None

    @property
    def visitor_image(self):
        return self.visitor_team.image.url if self.visitor_team else None
    
    class Meta:
        verbose_name = "Resultado"
        verbose_name_plural = "Resultados"

    def __str__(self) -> str:
        return self.event_name