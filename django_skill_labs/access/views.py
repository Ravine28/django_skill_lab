from django.http import HttpResponse
from django.template import loader
from .models import Access, Client, System

def access(request):
  access_list_html = Access.objects.all().values()
  template = loader.get_template('access_all.html')
  context = {
    'access_list_html': access_list_html,
  }
  return HttpResponse(template.render(context, request))

def access_details(request, id):
  acesso = Access.objects.get(id=id)
  template = loader.get_template('access_details.html')
  context = {
    'access': acesso,
  }
  return HttpResponse(template.render(context, request))