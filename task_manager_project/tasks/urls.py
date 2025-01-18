from django.urls import path
from . import views

urlpatterns = [
    # Exemplu de ruta, actualizează cu vizualizările tale
    path('', views.index, name='index'),
]
