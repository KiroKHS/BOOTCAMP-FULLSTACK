from django.shortcuts import redirect, render
from .models import ListaDeseos, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
  productos = Producto.objects.all()
  return render(request, 'core/index.html', {'productos': productos})

@login_required(login_url='login')
def wishlist(request):
  productos = ListaDeseos.objects.filter(usuario=request.user)
  return render(request, 'core/wishlist.html', {'productos': productos})

def quitarDeLista(request, id):
  datos={}
  producto = Producto.objects.get(id=id)
  usuario = request.user
  lista = ListaDeseos.objects.get(usuario=usuario, producto=producto)
  lista.delete()
  datos['msg'] = 'Se Quito el producto!.'
  datos['productos'] = ListaDeseos.objects.filter(usuario=request.user)
  return render(request, 'core/wishlist.html', datos)

def registro(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect(to='login')
  else:
    form = UserCreationForm()
  return render(request, 'core/registro.html', {'form': form})

def agregarALista(request, id):
  datos = {}
  #capturando datos del producto por id
  producto = Producto.objects.get(id=id)
  usuario = request.user
  datos['productos'] = Producto.objects.all()
  try:
    ListaDeseos.objects.get(producto=producto, usuario=usuario)
    datos["error"] = "producto ya se encuentra en lista de deseos"
    return render(request, 'core/index.html', datos )
  except ListaDeseos.DoesNotExist:
    lista = ListaDeseos(usuario=usuario, producto=producto)
    lista.save()
    datos["msg"] = 'Agregado a lista de deseos!.'
    return render(request, 'core/index.html', datos )

def getResultados(request):
  filtro = request.GET.get('filtro')
  productos = Producto.objects.filter(nombre=filtro)
  datos = {}
  datos['productos'] = productos
  return render(request, 'core/index.html', datos )
