from typing import Any, Dict
from django.views.generic import ListView, DeleteView, TemplateView, DetailView
from django.core.paginator import Paginator

from django.shortcuts import render
from .models import Home, News, Team, Video, Publicity
from applications.sports.models import Events, PrincipalEvent, Result
# Create your views here.


# home

class HomeView(TemplateView):

    template_name = "home/index.html"


    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        # Paginate
        posts = Home.objects.filter(active=True)
        paginator = Paginator(posts, 12)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)
        
        
        context["eventos"] = Events.objects.all().order_by("sport_category")
        context["evento_principal"] = PrincipalEvent.objects.filter(active=True).last()
        context["resultados"] = Result.objects.all().order_by("sport_category")
        context["noticia"] = News.objects.filter(breaking_new=True).last()
        context["video"] = Video.objects.filter(active=True).last()
        context["posts"] = page_object
        

        return context

class ArticleDetailView(DetailView):
    template_name = "home/articulo_detail.html"
    model = Home
    context_object_name = "articulo"

class PublicityDetailView(DetailView):
    template_name = "home/publicity_detail.html"
    model = Publicity
    context_object_name = "publicidad"

# Sobre Nosotros Pages
class ContactanosView(TemplateView):
    template_name = "sobre_nosotros/contactanos.html"

class QuienesSomosView(TemplateView):
    template_name = "sobre_nosotros/quienes_somos.html"

# Lista del equipo de trabajo

def team_list_view(request):
  
    team = Team.objects.all()

    return render(request, 'sobre_nosotros/team.html',{
      'team': team
        }
    )
