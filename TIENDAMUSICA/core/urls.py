from django.urls import path

from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('registro', registro, name='registro'),
    path('wishlist', wishlist, name='wishlist'),
    path('resultados/', getResultados, name='filtrar'),
    path('agregarALista/<id>', agregarALista, name='addTOList'),
    path('EliminarDeLista/<id>',quitarDeLista , name='deleteTOList'),
    path('login', LoginView.as_view(template_name="core/login.html"), name='login'),
    path('logout', LogoutView.as_view(template_name="core/logout.html"), name='logout'),
]
