from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Access, Client, System
from .forms import AccessForm, ClientForm, SystemForm
from .serializers import AccessSerializer, ClientSerializer, SystemSerializer


def home(request):
    return render(request, 'home.html')


def access(request):
    access = Access.objects.all()
    return render(request, 'access.html', {
        'access': access
    })

def access_details(request, id):
    access_details = get_object_or_404(Access, id=id)
    return render(request, 'access_details.html', {
        'access_details': access_details
    })

def access_create(request):
    if request.method == 'POST':
        form = AccessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('access_route')
    else:
        form = AccessForm()

    return render(request, 'form.html', {'form': form})

class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer

def client(request):
    client = Client.objects.all()
    return render(request, 'client.html', {
        'client': client
    })

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_route')
    else:
        form = ClientForm()

    return render(request, 'form.html', {'form': form})

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

def system(request):
    system = System.objects.all()
    return render(request, 'system.html', {
        'system': system
    })

def system_create(request):
    if request.method == 'POST':
        form = SystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('system_route')
    else:
        form = SystemForm()

    return render(request, 'form.html', {'form': form})

class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer