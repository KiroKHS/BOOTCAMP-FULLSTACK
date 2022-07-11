from django.db import models
#llamando datos del modelo usuario
from django.contrib.auth.models import User

#data table Categoria 
class Categoria(models.Model):
  nombreCategoria = models.CharField(max_length=20)
  def __str__(self) -> str:
      return self.nombreCategoria
#data table Producto 
class Producto(models.Model):
  nombre = models.CharField(max_length=40)
  descripcion = models.CharField(max_length=100)
  precio = models.IntegerField()
  imagen = models.ImageField(upload_to = "core/images")
  cateogria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
  def __str__(self) -> str:
      return self.nombre

# data table Lista deseos
class ListaDeseos(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

  def __str__(self) -> str:
      return self.usuario.username+ " "+self.producto.nombre

class Carrito(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
  
  def __str__(self) -> str:
     return f"{self.usuario.username} [{self.producto.nombre}] ${self.producto.precio}"