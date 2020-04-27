from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('empresa/', views.empresa, name='empresa'),
    path('empresa/<int:pk>/', views.EmpresaDetailView.as_view(), name='detail'),
    path('trabajadores/', views.trabajadores, name='trabajadores'),
]
