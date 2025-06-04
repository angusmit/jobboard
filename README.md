# Job Board MVP

A minimal job seeking website built with Django, similar to Indeed.

## Features
- Job listing and detail views
- Job posting form for employers
- Basic search functionality
- Admin approval system

## Installation
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## Access
- Homepage: http://localhost:8000/
- Admin: http://localhost:8000/admin/