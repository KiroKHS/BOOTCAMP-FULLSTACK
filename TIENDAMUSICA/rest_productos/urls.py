from django.urls import path
from .views import *

urlpatterns = [
    path('productos', productos),
    path('producto/<id>', producto),
]
