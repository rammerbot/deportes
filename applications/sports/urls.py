from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'sports_app'
urlpatterns = [
    path('sports/',views.sports_view, name="sports" ),
    path('news/', views.NewsView.as_view(), name="news"),
    path('new_detail/<slug:slug>/', views.new_detail_view, name="new_detail"),
    path('equipos/', views.TeamsView.as_view(), name="equipos"),
    path('equipos_detalles/', views.TeamsDetailViews.as_view(), name="equipos_detalles"),
    path('results/', views.sports_results_view, name="results"),
    path('eventos_list/<slug:slug>/', views.events_list_view, name="eventos_list"),
    
]
