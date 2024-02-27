from django.db import models


class NewsManager(models.Manager):

    def buscar_news(self, kword):
        return self.filter(title__icontains=kword, active=True).order_by('created')
        
    def buscar_breaking_news(self,kword):
        return self.filter(title__icontains=kword, active=True, breaking_new=True)