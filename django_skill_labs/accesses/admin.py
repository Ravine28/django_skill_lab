from django.contrib import admin
from .models import System, Client, Access

@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ("client", "system", "granted_at", "revoked_at")
    list_filter = ("system", "revoked_at")
    search_fields = ("client__name", "system__name")

'''admin.site.register(System) # Registra o model System para que ele possa ser gerenciado através do admin do Django
admin.site.register(Client) # Registra o model Client para que ele possa ser gerenciado através do admin do Django
admin.site.register(Access) # Registra o model Access para que ele possa ser gerenciado através do admin do Django'''
