from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Arepaso/', include('Arepaso.urls')),
    path('', include('Arepaso.urls'))
]
