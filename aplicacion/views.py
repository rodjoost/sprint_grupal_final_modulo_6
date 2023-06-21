from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Proovedor, Factura, Consumidor
from django.contrib import messages
from .forms import UserRegistrationForm, FacturaForm, ConsumidorForm, ProovedorForm
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


