from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('esto-es-una-prueba/', views.prueba, name='prueba'),
]
