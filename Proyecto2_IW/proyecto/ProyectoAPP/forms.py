from django.forms import ModelForm
from ProyectoAPP.models import Clientes


class FormModCliente(ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'


