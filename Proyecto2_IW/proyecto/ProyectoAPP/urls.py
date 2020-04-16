from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('entrar/', views.login, name="entrar"),
    path('PaginaPrincipal/', views.PaginaPricipal, name="PaginaPrincipal"),
    path('Registro/', views.LlamarFormulario, name="LlamarFormulario"),
    path('Registrar/', views.RecogerFormulario, name="RecogerFormulario"),
    path('DetallesProyecto', views.DetallesProyecto, name="DetallesProyecto")
]
