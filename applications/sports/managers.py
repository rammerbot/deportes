from django.db import models

from django.apps import apps


class EventManager(models.Manager):

    # Extraer eventos segun la categoria

    def event_by_category(self):
        sports = apps.get_model('sports', 'Sports')  # Obtener el modelo Sports

        sports_category ={

        }

        for sport_atr in sports.objects.all():
            
            sports_category[sport_atr.sport] = self.filter(sport = sport_atr.id)

        return sports_category