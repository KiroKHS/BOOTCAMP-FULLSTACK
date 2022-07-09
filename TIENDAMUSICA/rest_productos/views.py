from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view 
from core.models import Producto
from .serealizers import ProductorSerealizer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
@api_view(['GET', 'POST'])
def productos(request):
  if request.method == 'GET':
    productos = Producto.objects.all()
    serealizer = ProductorSerealizer(productos, many=True)
    return Response(serealizer.data)
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serealizer = ProductorSerealizer(data=data)
    if serealizer.is_valid():
      serealizer.save()
      return Response(serealizer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serealizer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def producto(request,id):
  try:
    producto = Producto.objects.get(id=id)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    serealizer = ProductorSerealizer(producto)
    return Response(serealizer.data)
  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serealizer = ProductorSerealizer(producto, data=data)
    if serealizer.is_valid():
      serealizer.save()
      return Response(serealizer.data, status=status.HTTP_202_ACCEPTED)
    else:
      return Response(serealizer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    producto.delete()
    return Response(serealizer.errors, status=status.HTTP_204_NO_CONTENT)
