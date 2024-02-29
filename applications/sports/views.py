from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Sports, Events, Teams, Result, SportCategories
from applications.home.models import News


# Create your views here.

# deportes Page
def sports_view(request):
    kwords = request.GET.get('kwords')
    deporte_seleccionado = request.GET.get('deporte')
    categorias = Sports.objects.all()
    eventos_por_categoria = {}

    for categoria in categorias:
        if kwords:
            eventos = Events.objects.filter(
                Q(sport__sport__icontains=kwords) | 
                Q(description__icontains=kwords)|
                Q(home_team__name__icontains=kwords)|
                Q(visitor_team__name__icontains=kwords),
                sport=categoria
            )
        elif deporte_seleccionado:
            eventos = Events.objects.filter(sport=categoria, sport__sport=deporte_seleccionado)
        else:
            eventos = Events.objects.filter(sport=categoria)
            
        eventos_por_categoria[categoria.sport] = eventos

    return render(request, 'deportes/deportes.html', {'deportes': eventos_por_categoria})


# Proximos Eventos 
class NewsView(ListView):
    template_name = "news/news.html"
    model = Events
    context_object_name = "eventos"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kword = self.request.GET.get('kword','')

        # Paginate
        buscar_noticias = News.objects.buscar_news(kword)
        paginator = Paginator(buscar_noticias, 12)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context["noticia_importante"] = News.objects.buscar_breaking_news(kword)
        context["noticias"] = page_obj
        context["deportes"] = Sports.objects.all()
        context["resultados"] = Result.objects.all().order_by("date")

        return context
 
# Detalle de Evento
def new_detail_view(request, slug):
    new = get_object_or_404(News, slug=slug)

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

# deportes Page
def sports_results_view(request):
    kwords = request.GET.get('kwords')
    deporte_seleccionado = request.GET.get('deporte')
    categorias = Sports.objects.all()
    eventos_por_categoria = {}

    for categoria in categorias:
        if kwords:
            eventos = Result.objects.filter(
                Q(sport__sport__icontains=kwords) | 
                Q(description__icontains=kwords)|
                Q(home_team__name__icontains=kwords)|
                Q(visitor_team__name__icontains=kwords),
                sport=categoria
            )
        elif deporte_seleccionado:
            eventos = Result.objects.filter(sport=categoria, sport__sport=deporte_seleccionado)
        else:
            eventos = Result.objects.filter(sport=categoria)
            
        eventos_por_categoria[categoria.sport] = eventos

    return render(request, 'resultados/resultados_list.html', {'deportes': eventos_por_categoria})



# Lista de proximos eventos por categorias

def events_list_view(request, pk):
  
    eventos = Events.objects.filter(sport_category_id = pk).order_by('created')

    return render(request, 'news/news_list.html',{
      'eventos':eventos  
        }
    )

