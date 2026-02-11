Notes of developer | Glossário

CAMPO = coluna da tabela
    ex: client_name = models.CharField
        resulta na criação de uma coluna "client_name" na tabela

LISTAGEM = query de vários registros
    Usualmente fica no arquivo views.py
    ex: client = Client.objects.all()
        resulta na bsuca de todos os clientes do banco

PROTEÇÃO DE VIEWS = somente usuários logados acessam
    ex: def access(request): //desprotegida
        
        @login_required  //protegida
        def access(request):

VIEWs vs FORMS    
    forms.py valida os dados inputados pelo user    --> analogia: formulário de papel preenchido
    views.py controla a lógica da page              --> analogia: atendente que avalia o formulário
    ex:
        forms.py
            class ClientForm(ModelForm): // define campos e regras
        views.py
            form = ClientForm(request.POST) // chama o forms





