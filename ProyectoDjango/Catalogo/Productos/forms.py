from django.forms import ModelForm #Modelo del formulario por defecto de django
from . import models               #Modelos de la aplicacion --> contiene las clases que vamos a importar

class FormProductos(ModelForm):
    class Meta:
        model = models.Producto    # Importa el modelo Producto
        fields =  '__all__'        # Este fields es para indicar que cuando renderice los campos, haga todos los campos que         tengan el modelo Producto que es el que importamos.
                                   # Si quiero q no sean todos , especifico ese dato mediante una lista de string 


## FormProductos es una clase y contiene como parametro un modelo que viene por defecto de django para formularios que es "ModelForm"                                 