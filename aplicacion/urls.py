from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.welcome, name='home'),
    path('factura/', views.factura, name="factura"), #endpoint
    path('consumidor/', views.consumidor, name="consumidor"),
    path('proveedor/', views.proveedor, name='proveedor'),
    path('register_user', views.register_user, name="register_user"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
