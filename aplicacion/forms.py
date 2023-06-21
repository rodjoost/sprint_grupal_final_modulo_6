from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission
from .models import Factura, Consumidor, Proveedor

class FacturaForm(forms.ModelForm):

    class Meta:
        model = Factura 
        fields = '__all__'

class ConsumidorForm(forms.ModelForm):
    class Meta:
        model = Consumidor
        fields = ['nombre', 'rut', 'giro', 'direccion', 'comuna','ciudad','tipo_compra']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['rut','razon','giro', 'direccion', 'email','telefono','tipo_venta']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmacion contraseña", widget=forms.PasswordInput)
    date = forms.DateField()
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class LoginForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)