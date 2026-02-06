# Django Skill Lab

## Descrição do Projeto

Este projeto se trata de um laboratório prático em **Django** com **Django Rest Framework (DRF)** para criação e exposição de controle de acesso entre **Clientes** e **Sistemas**.

O objetivo é permitir:

* Cadastro de Clientes
* Cadastro de Sistemas
* Gerenciamento de Acessos (vínculo cliente ↔ sistema)

  * Select
  * Create
  * Revoke
  * Update
  * Delete

---

## Estrutura do Projeto — Stack

### Backend

* Python 3.13
* Django 6.0.1
* Django Rest Framework

### Frontend

* Templates Django

### Banco de Dados

* SQLite (local, para desenvolvimento)

Este repositório segue a estrutura padrão de um projeto Django, separando claramente **configuração**, **aplicação** e **dados**.

---

## Arquivos principais

### manage.py

Script de gerenciamento do Django.

Usado para executar comandos administrativos como:

* Rodar o servidor - python manage.py runserver
* Criar migrations - python manage.py makemigrations
* Aplicar migrations - python manage.py migrate
* Criar superusuários - python manage.py createsuperuser

Funciona como o ponto de entrada para interação com o projeto.

---

### db.sqlite3

Banco de dados local utilizado durante o desenvolvimento.

* Baseado em arquivo (serializer: JSON)
* Adequado para aprendizado e prototipagem
* Em produção, normalmente substituído por PostgreSQL

---

## Projeto: django_skill_lab/

Diretório responsável pelas **configurações globais** do Django.
Não contém regras de negócio.

Armazena:

* django_skill_labs
* README.md
* .git
* .gitignore
* .venv

### settings.py

Arquivo central de configuração do projeto.

Diretório: django_skill_lab/django_skill_labs/django_skill_labs

Define:

* Aplicações instaladas
* Banco de dados
* Middlewares
* Segurança
* Idioma e timezone

---

### urls.py

Define o roteamento da aplicação.

Diretório: django_skill_lab/django_skill_labs/django_skill_labs

* Mapeia URLs para views
* Determina qual lógica será executada para cada caminho

---

### wsgi.py

Diretório: django_skill_lab/django_skill_labs/django_skill_labs

Ponto de entrada para servidores web tradicionais em produção.

Permite que servidores como:

* Gunicorn
* uWSGI

se comuniquem com o Django.

---

### asgi.py

Diretório: django_skill_lab/django_skill_labs/django_skill_labs

Ponto de entrada para servidores assíncronos.

Usado em aplicações que exigem:

* Comunicação em tempo real
* WebSockets

---

## Aplicações (apps)

Um app Django representa um **módulo funcional** da aplicação.
Cada app deve resolver um problema específico.

Diretório: django_skill_lab/django_skill_labs/

Armazena:

* admin.py
* apps.py
* __init__.py
* migrations
* models.py
* __pycache__
* templates
* tests.py
* urls.py
* views.py

Estrutura:

```
app_django_lab/
app_clientes/
app_sistemas/
app_acessos/
```

### apps.py

Diretório: django_skill_lab/django_skill_labs/app_django_lab

Configuração básica do app.

* Define nome
* Define metadados usados pelo Django

---

### models.py

Diretório: django_skill_lab/django_skill_labs/app_django_lab

Define os modelos de dados da aplicação.

* Cada modelo representa uma tabela
* Contém regras relacionadas aos dados

---

### views.py

Diretório: django_skill_lab/django_skill_labs/app_django_lab

Contém a lógica que processa requisições HTTP.

Fluxo:

1. Recebe a requisição
2. Executa a lógica
3. Retorna resposta

---

### admin.py

Diretório: django_skill_lab/django_skill_labs/app_django_lab

Configura como os modelos aparecem no painel administrativo.

Permite:

* Gerenciar dados
* Testar o sistema
* Evitar criar interfaces manuais

---

### tests.py

Diretório: django_skill_lab/django_skill_labs/app_django_lab

Contém testes automatizados.

Objetivos:

* Validar comportamento
* Evitar regressões

---

### migrations/

Diretório: django_skill_lab/django_skill_labs/app_django_lab

Armazena o histórico de alterações no banco de dados.

* Cada migration representa uma mudança estrutural

---

## Como subir o projeto localmente

### 1. Clonar o repositório

```bash
git clone git@github.com:Ravine28/django_skill_lab.git
cd django_skill_lab
```

> Cadastre a chave SSH e vincule ao seu ambiente local.

---

### 2. Criar e ativar o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install django
pip install djangorestframework
pip install -r requirements.txt
```

---

### 4. Rodar migrations

```bash
python manage.py migrate
```

> Certifique-se de estar no diretório onde o arquivo `manage.py` está.

---

### 5. Criar superusuário (opcional)

Usuário com acesso total ao painel administrativo.

Usado para:

* Entrar no `/admin`
* Criar dados manualmente
* Testar o sistema sem API ou frontend
* Gerenciar usuários e permissões

```bash
python manage.py createsuperuser
```

---

### 6. Subir o servidor

Liga um servidor local:

* Abre uma porta (geralmente 8000)
* Fica aguardando requisições

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000
```

---

## Variáveis de ambiente

Objetivo:

* Proteger dados sensíveis
* Evitar que credenciais sejam enviadas ao GitHub

Exemplo de variáveis:

* SECRET_KEY
* DEBUG
* DATABASE_URL

---

## Fluxo Git resumido

### 1. Criar nova branch

Não é boa prática desenvolver diretamente na `main`.

```bash
git switch main
git pull origin main
git switch -c tipo-feature/nome-da-feature
```

---

### 2. Commit

Após desenvolver o código:

```bash
git add .
git commit -m "feature: breve descrição da alteração"
```

---

### 3. Enviar para o GitHub

```bash
git push -u origin tipo-feature/nome-da-feature
```

Depois:

* Abrir Pull Request no GitHub
* Revisar
* Fazer merge na `main`
