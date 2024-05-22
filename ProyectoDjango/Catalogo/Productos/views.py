from django.shortcuts import render

# Create your views here.
def prods(request):
    return render(request, 'Productos/prod.html')

