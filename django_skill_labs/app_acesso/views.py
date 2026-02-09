from django.http import HttpResponse
from django.template import loader
from .models import Acesso

def acesso(request):
  acessos_html = Acesso.objects.all().values()
  template = loader.get_template('all_acess.html')
  context = {
    'acessos_html': acessos_html,
  }
  return HttpResponse(template.render(context, request))