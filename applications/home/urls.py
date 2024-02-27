from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'home_app'
urlpatterns = [
    path('',views.HomeView.as_view(), name="index" ),
    path('article_detail/<slug:slug>/', views.ArticleDetailView.as_view(), name="article_detail"),
    path('publicity_detail/<slug:slug>/', views.PublicityDetailView.as_view(), name="publicity_detail"),
    path('about/', views.QuienesSomosView.as_view(), name="about"),
    path('contact', views.ContactanosView.as_view(), name="contact"),
    path('team', views.team_list_view, name="team"),    
 
]
