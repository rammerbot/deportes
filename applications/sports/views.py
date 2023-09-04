from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Sports, Events, Teams, Result, SportCategories

# Create your views here.

# deportes Page
class SportView(ListView):

    template_name = "deportes/deportes.html"
    model = Sports
    context_object_name = 'deportes'


# Proximos Eventos 
class EventsView(ListView):
    template_name = "eventos/eventos.html"
    model = Events
    context_object_name = "eventos"

# Detalle de Evento
def event_detail_view(request, pk):
    evento = get_object_or_404(Events, id=pk)

    return render(request, "eventos/eventos_detail.html", {
        "evento":evento,
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

    return render(request, 'eventos/eventos_list.html',{
      'eventos':eventos  
        }
    )