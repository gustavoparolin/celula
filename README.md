# Celula Project

## Initial Setup (First Time Only)

1. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Create PostgreSQL database:
- Open pgAdmin 4
- Create new database named 'celula_db'
- Make sure PostgreSQL service is running

4. Create/update .env file with your database credentials:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DB_NAME=celula_db
DB_USER=postgres
DB_PASSWORD=your-password-here
DB_HOST=localhost
DB_PORT=5432
```

5. Run database migrations:
```bash
python manage.py migrate
```

## Daily Startup Commands

1. Start PostgreSQL Service:
   - Open Services (services.msc)
   - Find "postgresql-x64-17"
   - Make sure it's running (Start if needed)

2. Activate virtual environment (if not already activated):
```bash
.\venv\Scripts\activate
```

3. Start Django development server:
```bash
python manage.py runserver
```

4. Access the application:
   - Open browser and go to: http://localhost:8000

## Additional Commands

- Create a new Django app:
```bash
python manage.py startapp app_name
```

- Create database migrations:
```bash
python manage.py makemigrations
```

- Create a superuser (admin):
```bash
python manage.py createsuperuser
```

- Run Django shell:
```bash
python manage.py shell
```

## Current Stack
- Python 3.13.3
- Django 5.0.x
- PostgreSQL 17
- Tailwind CSS (in progress)

## Project Structure
- `config/` - Main project configuration
- `core/` - Core application with base templates
- `manage.py` - Django management script
- `requirements.txt` - Python dependencies