from django.shortcuts import render
from . forms import FormProductos

# Create your views here.
def prods(request):
    return render(request, 'Productos/prod.html')

def crearProducto(request):

    formulario = FormProductos()        #Instancia de un formulario

    contexto = {
        'titulo' : 'Crear Producto',
        'form' : formulario 
    }

    return render(request, 'Productos/crear.html', contexto)