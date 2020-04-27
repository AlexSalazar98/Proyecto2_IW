from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")


def prueba(request):
    return HttpResponse("Hola, esto es la prueba")
