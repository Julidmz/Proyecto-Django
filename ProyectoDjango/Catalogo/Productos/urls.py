from django.urls import path

from . import views

urlpatterns = [
    path('productos', views.prods),
    path('crearProducto', views.crearProducto, name='crearProducto')
]