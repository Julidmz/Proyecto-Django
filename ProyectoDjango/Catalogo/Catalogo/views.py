from django.shortcuts import render 

def home(request):
    return render(request, 'Catalogo/index.html')


# Este archivo tiene todos los controladores del proyecto catalogo

# Request es un objeto que me trae informacion de la peticion q se hace por http

# Todas las funciones que se hacen en este archivo tienen q tener un return con un response de algun tipo