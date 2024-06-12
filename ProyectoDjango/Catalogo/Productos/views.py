from django.shortcuts import render, HttpResponse, redirect
from . forms import FormProductos # Importamos el modelo FormProductos
from . models import Producto     #Importamos el modelo Producto

#-------------------------------------------------------------------------------------------------------------------------

# Create your views here.

def prods(request):
    return render(request, 'Productos/prod.html')

#-------------------------------------------------------------------------------------------------------------------------

# CREATE

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

        if formPost.is_valid():               #Este metodo es propio del formulario basado en modelos
            formPost.save()                   #Este es un metodo del modelo y a su vez tambien hace uso del ORM

            return redirect('listarProducto')
        else:
            return HttpResponse('error no guardado')
        
    else:
        return render(request, 'Productos/crear.html', contexto)
    


#is_valid() es un metodo que viene por defecto del formulario que ofrece django
#.save es un metodo que viene por defecto del formulario que ofrece django

#-------------------------------------------------------------------------------------------------------------------------

# READ

def listarProductos(request):
    productos = Producto.objects.all()  #Nos permite acceso al ORM y nos devuelve todos los objetos
    print(type(productos))

    contexto = {
        'productos': productos,
        'titulo': 'Listado de Productos'
    }

    return render(request, 'Productos/lista.html', contexto)

#-------------------------------------------------------------------------------------------------------------------------

# EDITAR

def editarProducto(request, id):
    
    productoEditar = Producto.objects.get(pk=id)

    if request.method == 'GET':
    #Se crea una instancia del formulario pero pasandole como parametro
    #una instancia del modelo Producto que corresponde al obtenido en
    #la consulta a la base de datos.
        formEditar = FormProductos(instance=productoEditar)

        contexto = {
            'form': formEditar,
            'mensaje': 'Editar Producto'
        }

        return render(request, 'Productos/crear.html', contexto)
    else:
        #Si la peticion es por POST
        formGuardar = FormProductos(request.POST, instance=productoEditar)
        if formGuardar.is_valid():
            formGuardar.save()
            return redirect('listarProducto')
        else:
            return render(request, 'Productos/crear.html',
            {'form':formGuardar, 'mensaje':'Error - Editar Producto'})
        

#-------------------------------------------------------------------------------------------------------------------------

# DELETE

def borrarProducto(request, id):

    borrar = Producto.objects.get(pk=id)

    borrar.delete

    return redirect('listarProducto')

