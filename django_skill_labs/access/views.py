from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Access, Client, System
from .forms import AccessForm, ClientForm, SystemForm
from .serializers import AccessSerializer, ClientSerializer, SystemSerializer
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html')


#create, read, update, delete (CRUD)
# Read (ler os acessos) e fazer login
@login_required
def access(request):
    access = Access.objects.all()
    return render(request, 'access.html', {
        'access': access
    })


# Read (ler os detalhes de um acesso específico)
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
def access_revoke(request, id):
    access = get_object_or_404(Access, id=id)

    if request.method == 'POST':
        access.access_date = None  # Revoga o acesso definindo a data de acesso como None
        access.save()
        return redirect('access_route')

    return render(request, 'confirm_revoke.html', {'object': access})

# API REST (DRF)
class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer


# Read (ler os clientes)
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
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


# Read (ler os sistemas)
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


# API REST (DRF)
class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer