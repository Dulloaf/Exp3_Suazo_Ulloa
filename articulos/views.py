from django.shortcuts import render, redirect
from .models import Alimento, TipoMascota, Marca
from .forms import AlimentoForm,RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
"""from .models import Alimento,Marca,TipoMascota"""

# Create your views here.

def inicio(request):
    
    return render(request,'inicio.html')

def mision(request):
    
    return render(request,'mision.html')

def pago(request):
    
    return render(request,'pago.html')

def contactanos(request):
    
    return render(request,'contactanos.html')

def tienda(request):
    
    return render(request,'tienda.html')

def mostrarAdmin(request):
    articulos=Alimento.objects.all()
    datos={
        'articulos':articulos
    }
    return render(request,'mostrarAdmin.html', datos)

def mostrarUsuario(request):
    articulos=Alimento.objects.all()
    datos={
        'articulos':articulos
    }
    return render(request,'mostrarUsuario.html', datos)

@login_required
def mostrar1(request):
    articulos=Alimento.objects.raw('select * from articulos_alimento')
    datos={'alimentos': articulos}
    return render(request, 'mostrar1.html', datos)

def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario=RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect ('inicio')
        data["form"]=formulario   
    return render(request,'registration/registrar.html', data)

@login_required
def crear(request):
    if request.method=="POST":
        alimentoform = AlimentoForm(request.POST,request.FILES) #Asigna objeto alimentoform
        if alimentoform.is_valid():
            alimentoform.save() 
            return redirect ('mostrarAdmin')
    else:
        alimentoform=AlimentoForm() #Sino este crea uno nuevo
    return render(request, 'crear.html', {'alimentoform' : alimentoform})

@login_required
def eliminar(request, id):
    alimentoEliminado=Alimento.objects.get(cod=id) #buscamos un vehiculo por la patentes
    alimentoEliminado.delete()
    return redirect('mostrarAdmin')

@login_required
def modificar(request,id):
    alimentoModificado = Alimento.objects.get(cod=id)
    datos ={
        'form': AlimentoForm(instance=alimentoModificado)   #el objeto form llega al template
    }
    if request.method=="POST":          #modificamos backend con los cambios realizados
        formulario = AlimentoForm(request.POST,request.FILES, instance=alimentoModificado)
        if formulario.is_valid():
            formulario.save()           #modificamos el objeto
            return redirect('mostrarAdmin')
    return render(request,'modificar.html', datos)

"""
def mostrarUsuario(request):
    articulos=Alimento.objects.all()
    datos={
        'articulos':articulos
    }
    return render(request,'mostrarUsuario.html', datos)
"""

