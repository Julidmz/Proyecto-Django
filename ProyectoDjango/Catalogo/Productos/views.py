from django.shortcuts import render, HttpResponse
from . forms import FormProductos

# Create your views here.
def prods(request):
    return render(request, 'Productos/prod.html')

def crearProducto(request):

    formulario = FormProductos()        #Instancia de un formulario

    contexto = {
        'titulo' : 'Crear Producto',
        'form' : formulario ,
        'lista' : [5, 8 , 23, 56]
    }

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