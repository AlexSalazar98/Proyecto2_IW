from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('entrar/', views.login, name="entrar"),
    path('PaginaPrincipal/', views.PaginaPricipal, name="PaginaPrincipal"),
    path('Formulario/', views.Formulario, name="Formulario"),
]
