from django.contrib import admin
from .models import System, Client, Access

admin.site.register(System) # Registra o modelo Sistema para que ele possa ser gerenciado através do admin do Django
admin.site.register(Client) # Registra o modelo Cliente para que ele possa ser gerenciado através do admin do Django
admin.site.register(Access) # Registra o modelo Acesso para que ele possa ser gerenciado através do admin do Django
