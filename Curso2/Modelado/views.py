from django.shortcuts import render
from Modelado.models import Restaurante, Platillo,FormularioRestauranteForm
# Create your views here.

def VistaMostrarRestaurantes(request):
    contexto={}
    if request.method == 'POST':
        form=FormularioRestauranteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print "Salve el objeto"
            response contexto["answer"]="True"
            
        else:
            print "NO ES VALIDOo"
            
    listado_restaurantes=Restaurante.objects.all()
    listado_platillos=Platillo.objects.all()
    contexto['listado_restaurantes']=listado_restaurantes
    contexto['listado_platillos']=listado_platillos
    return render(request, 'Front/index.html',contexto)