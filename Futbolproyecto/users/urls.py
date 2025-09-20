from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_equipo, name='crear_equipo'),
]