from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Sports, Events, Teams, Result, SportCategories
from applications.home.models import News

# Create your views here.

# deportes Page
class SportView(ListView):

    template_name = "deportes/deportes.html"
    model = Sports
    context_object_name = 'deportes'


# Proximos Eventos 
class NewsView(ListView):
    template_name = "news/news.html"
    model = Events
    context_object_name = "eventos"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kword = self.request.GET.get('kword','')
        context["articulos_1"] = News.objects.buscar_breaking_news(kword)
        context["articulos"] = News.objects.buscar_news(kword)
        context["deportes"] = Sports.objects.all()
        context["resultados"] = Result.objects.all().order_by("date")

        return context
 
# Detalle de Evento
def new_detail_view(request, pk):
    new = get_object_or_404(News, id=pk)

    return render(request, "news/news_detail.html", {
        "new":new,
    })    

# lista de Equipos
class TeamsView(ListView):
    template_name = "equipos/equipos.html"
    model = Teams
    context_object_name = "equipos"

# Detalle de Equipos
class TeamsDetailViews(DetailView):
    template_name = "equipos/equipos_detail.html"
    model = Teams
    context_object_name = "equipo"

# Resultados

class SportsResultsView(ListView):
    template_name = "resultados/resultados.html"
    model = Sports
    context_object_name = "deportes"
    
def results_list_view(request, pk):
    
    resultados = Result.objects.filter(sport_category_id = pk)

    return render(request, "resultados/resultados_list.html", {
        "resultados":resultados,
    })


# Lista de proximos eventos por categorias

def events_list_view(request, pk):
  
    eventos = Events.objects.filter(sport_category_id = pk).order_by('created')

    return render(request, 'news/news_list.html',{
      'eventos':eventos  
        }
    )

