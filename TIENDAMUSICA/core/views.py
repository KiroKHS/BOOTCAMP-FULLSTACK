from django.shortcuts import redirect, render
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
  productos = Producto.objects.all()
  return render(request, 'core/index.html', {'productos': productos})

def registro(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect(to='login')
  else:
    form = UserCreationForm()
  return render(request, 'core/registro.html', {'form': form})
