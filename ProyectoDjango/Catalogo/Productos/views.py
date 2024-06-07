from django.shortcuts import render, HttpResponse
from . forms import FormProductos # Importamos el modelo FormProductos
from . models import Producto     #Importamos el modelo Producto

#-------------------------------------------------------------------------------------------------------------------------

# Create your views here.

def prods(request):
    return render(request, 'Productos/prod.html')

#-------------------------------------------------------------------------------------------------------------------------

# Create 

def crearProducto(request):

    formulario = FormProductos()        #Instancia de un formulario

    contexto = {
        'titulo' : 'Crear Producto',
        'form' : formulario ,
        'lista' : [5, 8 , 23, 56]
    }

    #El diccionario "contexto" me sirve para mandar estructuras de datos del back al front --> el formulario
    #Es el tercer argumento q le paso al metodo render: (request, template, contexto)
    #A traves del metodo render estoy enviando esos argumentos al frontend

    if(request.method == 'POST'): 
        #return HttpResponse('PETICION POR POST')
        formPost = FormProductos(request.POST)

        if formPost.is_valid():    
            formPost.save()

            return HttpResponse('guardado ok')
        else:
            return HttpResponse('error no guardado')
        
    else:
        return render(request, 'Productos/crear.html', contexto)
    


#is_valid() es un metodo que viene por defecto del formulario que ofrece django
#.save es un metodo que viene por defecto del formulario que ofrece django

#-------------------------------------------------------------------------------------------------------------------------

# Read

def listarProductos(request):
    productos = Producto.objects.all()  #Nos permite acceso al ORM
    print(type(productos))

    context = {
        'productos': productos,
        'titulo': 'Listado de Productos'
    }

    return render(request, 'Productos/lista.html', context)

