from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('Entrar/', views.login, name="Entrar"),
    path('PaginaPrincipal/', views.PaginaPricipal, name="PaginaPrincipal")
]
