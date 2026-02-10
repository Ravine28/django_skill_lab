from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import Access, Client, System

def access(request):
  access_list_html = Access.objects.all()
  template = loader.get_template('access_all.html')
  context = {
    'access_list_html': access_list_html,
  }
  return HttpResponse(template.render(context, request))

def access_details(request, id):
  access_details_list_html = get_object_or_404(Access, id=id)
  template = loader.get_template('access_details.html')
  context = {
    'access_details_list_html': access_details_list_html,
  }
  return HttpResponse(template.render(context, request))

def system_access(request):
  system_access_list_html = System.objects.all()
  template = loader.get_template('system_access.html')
  context = {
    'system_access_list_html': system_access_list_html,
  }
  return HttpResponse(template.render(context, request))

def client_access(request):
  client_access_list_html = Client.objects.all()
  template = loader.get_template('client_access.html')
  context = {
    'client_access_list_html': client_access_list_html,
  }
  return HttpResponse(template.render(context, request))