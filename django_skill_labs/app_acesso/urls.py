from django.urls import path
from . import views

urlpatterns = [
    path('acesso/', views.acesso, name='acesso'),  
]
