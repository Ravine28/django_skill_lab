from django.urls import path # Função para definir (mapear --> apontar) rotas de URL
from . import views

'''
Sintaxe: path('caminho/', views.nome_da_view, name='nome_da_url')
    - 'caminho/': O caminho da URL que será acessada no navegador.
    - views.nome_da_view: A função ou classe de visualização que será chamada quando a URL for acessada.
    - name='nome_da_url': Um nome opcional para a URL, que pode ser usado para referenciar a URL em outras
      partes do código, como em templates ou redirecionamentos.

URL dinâmica para acessar os detalhes de um acesso específico, onde <int:id> é um parâmetro de URL que captura 
um valor inteiro (id do acesso) e o passa para a view access_details como uma variável.
    - int: é o conversor. ELe garante que a rota só funcione se o usuário informar um valor inteiro
    - id: variável que armazena o número de referência do acesso. É passado para a view access_details como uma variável
'''


urlpatterns = [ # Lista de URLs para Apps access, onde cada URL é associada a uma view
    path ('', views.home, name='home'),

    # Access
    path('acesso/', views.access, name='access'),
    path('acesso/<int:id>/', views.access_details, name='access_details'),
    path('acesso/novo/', views.access_create, name='access_create'),
    path('acesso/atualizar/<int:id>/', views.access_update, name='access_update'),
    path('acesso/excluir/<int:id>/', views.access_delete, name='access_delete'),
    path('acessos/<int:id>/revogar/', views.access_revoke, name='access_revoke'),



    # Client
    path('clientes/', views.client, name='client'),
    path('clientes/novo/', views.client_create, name='client_create'),
    path('clientes/atualizar/<int:id>/', views.client_update, name='client_update'),
    path('clientes/excluir/<int:id>/', views.client_delete, name='client_delete'),

    # System
    path('sistemas/', views.system, name='system'),
    path('sistemas/novo/', views.system_create, name='system_create'),
    path('sistemas/atualizar/<int:id>/', views.system_update, name='system_update'),
    path('sistemas/excluir/<int:id>/', views.system_delete, name='system_delete'),

    # Registration
    path('register/', views.register, name='register'),
]
