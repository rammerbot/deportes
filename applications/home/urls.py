from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'home_app'
urlpatterns = [
    path('',views.HomeView.as_view(), name="index" ),
    path('articulo_detail/<pk>/', views.ArticleDetailView.as_view(), name="articulo_detail"),
    path('quienes_somos/', views.QuienesSomosView.as_view(), name="quienes_somos"),
    path('contactanos', views.ContactanosView.as_view(), name="contactanos"),
    
 
]
