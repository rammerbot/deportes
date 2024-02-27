from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'sports_app'
urlpatterns = [
    path('deportes/',views.SportView.as_view(), name="deportes" ),
    path('news/', views.NewsView.as_view(), name="news"),
    path('new_detail/<slug:slug>/', views.new_detail_view, name="new_detail"),
    path('equipos/', views.TeamsView.as_view(), name="equipos"),
    path('equipos_detalles/', views.TeamsDetailViews.as_view(), name="equipos_detalles"),
    path('resultados/', views.SportsResultsView.as_view(), name="resultados"),
    path('resultados_list/<pk>/', views.results_list_view, name="resultados_list"),
    path('eventos_list/<slug:slug>/', views.events_list_view, name="eventos_list"),
    
]
