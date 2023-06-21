from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Proveedor, Factura, Consumidor
from django.contrib import messages
from .forms import UserRegistrationForm, FacturaForm, ConsumidorForm, ProveedorForm
# Create your views here.

def welcome(request):
    return render(request, "home.html")

def factura(request):
    form = FacturaForm()
    if request.method == "POST":
        form = FacturaForm(request.POST)
        if form.is_valid():
            print(form)
            factura = Factura()
            factura.n_factura = form.cleaned_data['n_factura']
            factura.producto = form.cleaned_data['producto']
            factura.cantidad = form.cleaned_data['cantidad']
            factura.neto = form.cleaned_data['neto']
            factura.iva = form.cleaned_data['iva']
            factura.total = form.cleaned_data['total']
            factura.fecha_emision =form.cleaned_data['fecha_emision']
            factura.save()
        else:
            print("Datos invalidos")
        return redirect('/factura')
    context = {'form': form}

    return render(request, 'factura.html', context=context)
@login_required
def consumidor(request):
    form = ConsumidorForm()
    if request.method == "POST":
        form = ConsumidorForm(request.POST)
        if form.is_valid():
            print(form)
            consumidor = Consumidor()
            consumidor.nombre = form.cleaned_data['nombre']
            consumidor.rut = form.cleaned_data['rut']
            consumidor.giro = form.cleaned_data['giro']
            consumidor.direccion = form.cleaned_data['direccion']
            consumidor.comuna= form.cleaned_data['comuna']
            consumidor.ciudad = form.cleaned_data['ciudad']
            consumidor.tipo_compra =form.cleaned_data['tipo_compra']
            consumidor.save()
        else:
            print("Datos invalidos")
        return redirect('/consumidor')
    context = {'form': form}

    return render(request, 'consumidor.html', context=context)
@login_required
def proveedor(request):
    form = ProveedorForm()
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            print(form)
            proveedor = Proveedor()
            proveedor.rut = form.cleaned_data['rut'] 
            proveedor.razon= form.cleaned_data['razon']
            proveedor.giro = form.cleaned_data['giro']
            proveedor.direccion = form.cleaned_data['direccion']
            proveedor.email= form.cleaned_data['email']
            proveedor.telefono = form.cleaned_data['telefono']
            proveedor.tipo_venta =form.cleaned_data['tipo_venta']
            proveedor.save()
        else:
            print("Datos invalidos")
        return redirect('/proveedor')
    context = {'form': form}

    return render(request, 'proveedor.html', context=context)

@login_required
def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            permissions = form.cleaned_data['permissions']
            username = form.cleaned_data['username']
            user.groups.add(group)
            user.user_permissions.set(permissions)
            messages.success(request, f'Usuario {username} creado exitosamente!!')
            return redirect('/home')
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'register_user.html', context)

        

