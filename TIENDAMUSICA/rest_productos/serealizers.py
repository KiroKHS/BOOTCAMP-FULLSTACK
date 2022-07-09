from rest_framework.serializers import ModelSerializer
from core.models import *

class ProductorSerealizer(ModelSerializer):
  class Meta:
    model = Producto
    fields = ['id', 'nombre', 'descripcion', 'precio', 'imagen', 'cateogria']
