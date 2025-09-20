# users/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('crear/', views.crear_equipo, name='crear_equipo'),
    path('lista/', views.lista_equipos, name='lista_equipos'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]