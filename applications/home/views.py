from typing import Any, Dict
from django.views.generic import ListView, DeleteView, TemplateView, DetailView

from django.shortcuts import render
from .models import Home, Articles
# Create your views here.


# home

class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        context["articulos"] = Articles.objects.filter(active =  True)
        context["homes"] = Home.objects.filter(active = True)
        
        return context

class ArticleDetailView(DetailView):
    template_name = "home/articulo_detail.html"
    model = Articles
    context_object_name = "articulo"

# Sobre Nosotros Pages
class ContactanosView(TemplateView):
    template_name = "sobre_nosotros/contactanos.html"

class QuienesSomosView(TemplateView):
    template_name = "sobre_nosotros/quienes_somos.html"
