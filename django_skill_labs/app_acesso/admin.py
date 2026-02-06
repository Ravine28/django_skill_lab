from django.contrib import admin
from .models import Sistema, Cliente

admin.site.register(Sistema) # Registra o modelo Sistema para que ele possa ser gerenciado através do admin do Django
admin.site.register(Cliente) # Registra o modelo Cliente para que ele possa ser gerenciado através do admin do Django
