from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import ProveedorForm

# Create your views here.

def Paginaprincipal(request):

    return render(request, 'Paginaprincipal.html'

      

    )

def Productos(request):

    return render(request, 'Productos.html'

      

    )

def QuienesSomos(request):

    return render(request, 'QuienesSomos.html'

      

    )

def Registro(request):

    return render(request, 'Registro.html'

      

    )

def Despacho(request):

    return render(request, 'Despacho.html'

      

    )

def Proveedores(request):

    proveedores = Proveedor.objects.all
    return render(request, 'GreenPanda/Proveedores.html', context ={ 'datos':proveedores}

      

    )

def CrearProveedores(request):
    if request.method=='POST':
        proveedor_form = ProveedorForm(request.POST, files=request.FILES)
        if proveedor_form.is_valid():
            proveedor_form.save()
            return redirect('Proveedores')
    else:
        proveedor_form= ProveedorForm()
    return render(request, 'GreenPanda/CrearProveedores.html', {'proveedor_form': proveedor_form}

      

    )

def ModProveedores(request,id):
    prov = Proveedor.objects.get(numId=id)

    pro ={
        'form': ProveedorForm(instance=prov)
    }
    if request.method=='POST':
        formulario = ProveedorForm(data=request.POST, instance = prov, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            return redirect('Proveedores')
        pro['form'] = formulario
    
    
    return render(request, 'GreenPanda/ModProveedores.html', pro
    
    
    
    )

def eliminar(request,id):
    prov = Proveedor.objects.get(numId=id)
    prov.delete()
    return redirect('Proveedores')