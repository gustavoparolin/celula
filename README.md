# Projeto Célula

## Configuração Inicial (Apenas Primeira Vez)

1. Criar e ativar ambiente virtual:
```bash
python -m venv venv
.\venv\Scripts\activate
```

2. Instalar dependências Python:
```bash
pip install -r requirements.txt
```

3. Criar banco de dados PostgreSQL:
- Abra o pgAdmin 4
- Crie um novo banco de dados chamado 'celula_db'
- Certifique-se que o serviço PostgreSQL está rodando

4. Criar/atualizar arquivo .env com suas credenciais de banco de dados:
```
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
DB_NAME=celula_db
DB_USER=postgres
DB_PASSWORD=sua-senha-aqui
DB_HOST=localhost
DB_PORT=5432
```

5. Executar migrações do banco de dados:
```bash
python manage.py migrate
```

## Comandos para Inicialização Diária

1. Iniciar Serviço PostgreSQL:
   - Abra Serviços (services.msc)
   - Localize "postgresql-x64-17"
   - Certifique-se que está rodando (Inicie se necessário)

2. Ativar ambiente virtual (se ainda não estiver ativado):
```bash
.\venv\Scripts\activate
```

3. Iniciar servidor de desenvolvimento Django:
```bash
python manage.py runserver
```

4. Acessar a aplicação:
   - Abra o navegador e acesse: http://localhost:8000

## Comandos Adicionais

- Criar uma nova aplicação Django:
```bash
python manage.py startapp nome_da_app
```

- Criar migrações do banco de dados:
```bash
python manage.py makemigrations
```

- Criar um superusuário (admin):
```bash
python manage.py createsuperuser
```

- Executar shell do Django:
```bash
python manage.py shell
```

## Stack Atual
- Python 3.13.3
- Django 5.0.x
- PostgreSQL 17
- Tailwind CSS (em desenvolvimento)

## Estrutura do Projeto
- `config/` - Configuração principal do projeto
- `core/` - Aplicação core com templates base
- `manage.py` - Script de gerenciamento Django
- `requirements.txt` - Dependências Python