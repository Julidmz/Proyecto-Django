from django.urls import path

from . import views

urlpatterns = [
    path('productos', views.prods),
    path('crearProducto', views.crearProducto, name='crearProducto'),
    path('listarProducto', views.listarProductos, name='listarProducto'),
    path('editarProducto/<int:id>', views.editarProducto, name='editarProducto'),
     path('borrarProducto/<int:id>', views.borrarProducto, name='borrarProducto')
]


# urlpatterns es una lista