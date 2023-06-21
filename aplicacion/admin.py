from django.contrib import admin
from .models import Factura, Consumidor, Proovedor
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Factura)
admin.site.register(Consumidor)
admin.site.register(Proovedor)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email')
    list_filter = ('is_staff', 'is_superuser')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

