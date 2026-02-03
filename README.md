## Estrutura do Projeto Django
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

## app_django_lab/ (Aplicação)
Um app Django representa um **módulo funcional** da aplicação.
Cada app deve resolver um problema específico.

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

### apps.py
Configuração básica do app.
Define nome e metadados utilizados pelo Django para registrar a aplicação.

---

### tests.py
Contém testes automatizados da aplicação.
Serve para validar comportamento e evitar regressões.

---

### migrations/
Armazena o histórico de alterações no banco de dados.
Cada migration representa uma mudança estrutural nos modelos.
