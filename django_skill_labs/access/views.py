from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from .forms import AccessForm, ClientForm, SystemForm, RegisterForm
from .models import Access, Client, System
from .serializers import AccessSerializer, ClientSerializer, SystemSerializer

'''
  Padrão mais aceito (PEP8 + Django) é: 
    # 1. Bibliotecas padrões Python
    # 2. Django (Bibliotecas do Framework)
    # 3. Third-party (Bibliotecas de terceiros)
    # 4. Local Apps (Arquivos do seu projeto)

'''

def home(request):
    return render(request, 'home.html')

#create, read, update, delete (CRUD) + revoke
# API REST (DRF)
class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer

# Read (ler os acessos) e fazer login
@login_required
def access(request):
    access = Access.objects.all()
    return render(request, 'access.html', {
        'access': access
    })

# Read (ler os detalhes de um acesso específico)
@login_required
def access_details(request, id):
    access_details = get_object_or_404(Access, id=id)
    return render(request, 'access_details.html', {
        'access_details': access_details
    })

# Create (criar um novo acesso)
def access_create(request):
    if request.method == 'POST':
        form = AccessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('access_route')
    else:
        form = AccessForm()

    return render(request, 'form.html', {'form': form})

# Update (atualizar um acesso existente)
def access_update(request, id):
    access = get_object_or_404(Access, id=id)

    if request.method == 'POST':
        form = AccessForm(request.POST, instance=access)
        if form.is_valid():
            form.save()
            return redirect('access_route')
    else:
        form = AccessForm(instance=access)

    return render(request, 'form.html', {'form': form})

# Delete (excluir um acesso existente)
def access_delete(request, id):
    access = get_object_or_404(Access, id=id)

    if request.method == 'POST':
        access.delete()
        return redirect('access_route')

    return render(request, 'confirm_delete.html', {'object': access})

# Revoke (revogar um acesso existente)
@require_POST # proteger contra requisições GET acidentais
def access_revoke(request, id):
    access = get_object_or_404(Access, id=id)
    access.is_active = False
    access.save()
    return redirect('access_route')

# API REST (DRF)
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Read (ler os clientes)
@login_required
def client(request):
    client = Client.objects.all()
    return render(request, 'client.html', {
        'client': client
    })

# Create (criar um novo cliente)
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_route')
    else:
        form = ClientForm()

    return render(request, 'form.html', {'form': form})

# Update (atualizar um cliente existente)
def client_update(request, id):
    client = get_object_or_404(Client, id=id)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_route')
    else:
        form = ClientForm(instance=client)

    return render(request, 'form.html', {'form': form})

# Delete (excluir um cliente existente)
def client_delete(request, id):
    client = get_object_or_404(Client, id=id)

    if request.method == 'POST':
        client.delete()
        return redirect('client_route')

    return render(request, 'confirm_delete.html', {'object': client})

# API REST (DRF)
class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer

# Read (ler os sistemas)
@login_required
def system(request):
    system = System.objects.all()
    return render(request, 'system.html', {
        'system': system
    })

# Create (criar um novo sistema)
def system_create(request):
    if request.method == 'POST':
        form = SystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('system_route')
    else:
        form = SystemForm()

    return render(request, 'form.html', {'form': form})

# Update (atualizar um sistema existente)
def system_update(request, id):
    system = get_object_or_404(System, id=id)

    if request.method == 'POST':
        form = SystemForm(request.POST, instance=system)
        if form.is_valid():
            form.save()
            return redirect('system_route')
    else:
        form = SystemForm(instance=system)

    return render(request, 'form.html', {'form': form})

# Delete (excluir um sistema existente)
def system_delete(request, id):
    system = get_object_or_404(System, id=id)

    if request.method == 'POST':
        system.delete()
        return redirect('system_route')

    return render(request, 'confirm_delete.html', {'object': system})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render(request))

def testing(request):
    template = loader.get_template('testing.html')
    context = {
        'message': 'Olá, esta é uma mensagem de teste!',
        'number': 42,
        'items': ['Galinha', 'Suricato', 'Macaco'],
    }
    return HttpResponse(template.render(context, request))

