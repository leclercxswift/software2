from django.shortcuts import render
from .models import Producto

# Create your views here.
def prod(request):
    productos = Producto.objects.all()
    return render(request,'producto.html',{'productos':productos})
def mostrar_productos(request):
    categoria_id = request.GET.get('categoria_id')
    if categoria_id:
        productos = Producto.objects.filter(category=categoria_id)
    else:
        productos = Producto.objects.all()
    return render(request, 'producto.html', {'productos': productos})
