# Django Skill Lab

## Descrição do Projeto
Este projeto se trata de um laboratório prático em Django com Django Rest Framework (DRF) para criação e exposição de uma API de controle de acesso entre Clientes e Sistemas.
    O objetivo é permitir:
    Cadastro de Clientes
    Cadastro de Sistemas
    Acessos (vínculo cliente-sistema)
        Select
        Create
        Revoke
        Update
        Delete

---

## Estrutura do Projeto - Stack (Django + Django Rest Framework)
### Backend

* Python 3.13
* Django 6.0.1
* Django Rest Framework

### Frontend
 * Tempĺate Django

### Banco de Dados
 * SQLite (Local)
Este repositório segue a estrutura padrão de um projeto Django, separando claramente **configuração**, **aplicação** e **dados**.
Abaixo está a função de cada diretório e arquivo principal.

---

### manage.py
Script de gerenciamento do Django.
É usado para executar comandos administrativos como:
- rodar o servidor
- criar migrations
- aplicar migrations
- criar superusuários
Funciona como o ponto de entrada para interação com o projeto.

---

### db.sqlite3
Banco de dados local utilizado durante o desenvolvimento.
É um banco baseado em arquivo, adequado para aprendizado e prototipagem.
Em ambientes de produção, normalmente é substituído por bancos como PostgreSQL.

---

## django_skill_labs/ (Projeto)
Diretório responsável pelas **configurações globais** do Django.
Ele não contém regras de negócio.

---

### settings.py
Arquivo central de configuração do projeto.
Define:
- aplicações instaladas
- banco de dados
- middlewares
- segurança
- idioma e timezone
Todas as decisões estruturais do projeto passam por aqui.

---

### urls.py
Define o roteamento da aplicação.
Mapeia URLs para views, determinando qual lógica será executada para cada caminho acessado.

---

### wsgi.py
Ponto de entrada para servidores web tradicionais em produção.
Permite que servidores como Gunicorn ou uWSGI se comuniquem com o Django.

---

### asgi.py
Ponto de entrada para servidores assíncronos.
Utilizado em aplicações que exigem comunicação em tempo real, como WebSockets.

---

## Aplicações (apps)
### apps.py
Configuração básica do app.
Define nome e metadados utilizados pelo Django para registrar a aplicação.

---

### app_django_lab/ 
Um app Django representa um **módulo funcional** da aplicação.
Cada app deve resolver um problema específico.

### app_clientes/

### app_sistemas/

### app_acessos/

---

### models.py
Define os modelos de dados da aplicação.
Cada modelo representa uma tabela no banco de dados e encapsula regras relacionadas aos dados.

---

### views.py
Contém a lógica que processa requisições HTTP.
Recebe a requisição, executa a lógica necessária e retorna uma resposta.

---

### admin.py
Configura como os modelos aparecem no painel administrativo do Django.
Permite gerenciar dados sem necessidade de criar interfaces manuais.

---

### tests.py
Contém testes automatizados da aplicação.
Serve para validar comportamento e evitar regressões.

---

### migrations/
Armazena o histórico de alterações no banco de dados.
Cada migration representa uma mudança estrutural nos modelos.

---

## Como subir projeto localmente
### 1. Clonar o  repositório
    git clone git@github.com:Ravine28/django_skill_lab.git 
    cd django_skill_lab

    OBS: cadastre a chave SSH e a vincule ao seu ambiente dev local

### 2. Criar e ativar o ambiente virtual (.venv)
    python3 -m venv .venv source 
    .venv/bin/activate

### 3. Instalar dependências
    pip install django
    pip install djangorestframework
    pip install -r requirements.txt

### 4. Rodar migrations
    python manage.py migrate
        * certifique-se de estar dentro do diretório onde o arquivo _manage.py_ está!

### 5. Criar superusuário (opcional)
    * Usuário com acesso total ao painel administrativo do Django. Utilizado para:
        - Entrar no /admin
        - Criar dados manualmente
        - Testar o sistema sem usar API ou frontend
        - Gerenciar usuários e permissões
    python manage.py createsuperuser

### 6. Subir o servidor
    - Liga um servidor local
    - Abre uma porta (geralmente 8000)
    - Fica esperando requisições
    python manage.py runserver

## Variáveis de ambiente
    * Proteger dados sensíveis evitando que as mesmas subam para GitHub

## Fluxo Git resumido
### Crie uma nova branch
    * Não é uma boa prática desenvolver utilizando a branch _main_
    git switch main 
    git pull origin main 
    git switch -c tipo-feature/nome-da-feature

### Commit
   * Após desenvolver o código
   git add .
   git commit -m "feature: breve descrição do commit(alteração)

### Atualizar repositório GitHub
    git push -u origin tipo-feature/nome-da-feature
    * Depois, abrir Pull Request no GitHub.
