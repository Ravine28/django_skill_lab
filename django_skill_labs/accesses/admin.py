from django.contrib import admin
from .models import System, Client, Access

@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ("client", "system", "granted_at", "revoked_at")
    list_filter = ("system", "revoked_at")
    search_fields = ("client__name", "system__name")

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
