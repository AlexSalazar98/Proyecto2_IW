from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Empresa, Trabajador


# Devuelve la página principal
def index(request):
    context = {
        'titulo_pagina': 'BIENVENID@',
        'bienvenida': "Bienvenido a la página"
    }
    return render(request, 'Bienvenida.html', context)


# Devuelve los nombres de todas la empresas
def empresa(request):
    empresas = Empresa.objects.order_by('nombre')
    context = {
        'titulo_pagina': 'Listado de empresas',
        'empresa_list': empresas
    }
    return render(request, 'Empresas.html', context)

#class EmpresaListView(ListView):
#    model = Empresa
#    template_name = 'Empresas.html'
#    queryset = Empresa.objects.order_by('nombre')

#    def get_context_data(self, **kwargs):
#        context = super(EmpresaListView, self).get_context_data(**kwargs)
#        context['titulo_pagina'] = 'Listado de empresas'
#        return context


# Devuelve los datos de cada empresa
#def details(request, empresa_id):
#    empresa = Empresa.objects.get(pk=empresa_id)
#    context = {
#        'titulo_pagina': 'Detalles de la empresa',
#        'empresa': empresa
#    }
#    return render(request, 'Detalles.html', context)

class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = 'Detalles.html'

    def get_context_data(self, **kwargs):
        context = super(EmpresaDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de la empresa'
        return context


# Devuelve los nombres de los trabajadores
def trabajadores(request):
    trabajadores = Trabajador.objects.order_by('nombre_trabajador')
    output = ', '.join(t.nombre_trabajador for t in trabajadores)
    return HttpResponse(output)
