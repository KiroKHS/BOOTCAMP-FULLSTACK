from django.db import models

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