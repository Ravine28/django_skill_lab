Notes of developer | Glossário

CAMPO

    coluna da tabela
    
    ex: 
    
        client_name = models.CharField
        
        resulta na criação de uma coluna/campo "client_name" na tabela/classe "client"

LISTAGEM

query de vários registros
    
    Usualmente fica no arquivo views.py
    ex: 
    
        client = Client.objects.all()
        
        resulta na bsuca de todos os clientes do banco

PROTEÇÃO DE VIEWS

somente usuários logados acessam
    
    ex: def access(request): //desprotegida
        
        @login_required  //protegida
        def access(request):

VIEWs vs FORMS    
    
    forms.py valida os dados inputados pelo user    --> analogia: formulário de papel preenchido
        e se chamar a form.save() , ele tbm salva no banco
    
    views.py controla a lógica da page              --> analogia: atendente que avalia o formulário
    
    ex:
        
        forms.py
            
            class ClientForm(ModelForm): // define campos e regras
        
        views.py
            
            form = ClientForm(request.POST) // chama o forms

VIEWSET (ModelViewSet)
    
    são tipos de classes que, através de mixins, ja entregam funções prontas como: listar - criar - atualizar - deletar
    
    class ModelViewSet(
        ListModelMixin,
        CreateModelMixin,
        RetrieveModelMixin,
        UpdateModelMixin,
        DestroyModelMixin,
        GenericViewSet
    )
    
    ex:
        
        class ClientViewSet(viewsets.ModelViewSet):
            queryset = Client.objects.all()
            serializer_class = ClientSerializer
        
        --> automaticamente o Django REST Framework irá criar:
                
                list()
                create()
                retrieve()
                update()
                partial_update()
                destroy()

--> DRF abstrai a lógica fazendo o CRUD sozinho

--> queryset + serializer montam CRUDs mais simples

--> método sbrescrito faz ajustes no comportamento padrão

--> mixins são pequenas funções que fazem ajustes pontuais ao ViewSet

MIXIN
    
    são pequenas classes que adicionam funções específicas

MÉTODOS HTTP PRINCIPAIS

    GET     --> busca(visualização) de dados    |   ex: abrir página
    
    POST    --> criação dados                   |   ex: enviar formulário
    
    PUT     --> atualização total               |   ex: atualização total de objeto via API
   
    PATCH   --> atualização parcial             |   ex: atualização parcial 
    
    DELETE  --> remoção de dados                |   ex: apagar registro
   
    HEAD    --> apenas verifica a existência    |   ex: checar tamanho de um arquivo
    
    OPTIONS --> descobrir métodos disponíveis   |   ex: usado por APIs


FUNÇÕES NO DRF

    ex: def destroy(self, request, *args, **kwargs):
        
        sintaxe: 

            self = instância da viewset

            request = requisição HTTP

            *args = argumentos posicionais

            **kwargs = argumentos nomeados (id_objeto)

