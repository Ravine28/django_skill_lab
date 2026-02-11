"""
URL configuration for django_skill_labs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from access.views import ClientViewSet, SystemViewSet, AccessViewSet

router = DefaultRouter()
router.register('clients', ClientViewSet)
router.register('systems', SystemViewSet)
router.register('access', AccessViewSet)

urlpatterns = [
    path('', include('access.urls')), # Se a URL estiver vazia, vá para a App "access" via access.urls
    path('admin/', admin.site.urls), # Se a URL iniciar em "admin/", vá para a interface padrão de administração do Django
    path('api/', include(router.urls)),
]
