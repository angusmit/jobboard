# Job Board MVP

A minimal job seeking website built with Django, similar to Indeed.

## Features

- Job listing and detail views

- Job posting form for employers

- Basic search functionality

- Admin approval system

- User authentication system:

- Separate signup for job seekers and employers

- Login/logout functionality

- Role-based permissions

- Job-employer relationship tracking

- Responsive UI with navigation

## Installation

```bash

# Create virtual environment

python -m venv venv

# Activate environment

# Windows:

venv\Scripts\activate

# Linux/Mac:

source venv/bin/activate

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

- **Homepage:** http://localhost:8000/

- **Admin:** http://localhost:8000/admin/

- **Signup:** http://localhost:8000/signup/

- **Login:** http://localhost:8000/login/

- **Post Job (requires login):** http://localhost:8000/post/

## User Roles

1. **Admin:**

- Approve/reject job postings

- Manage users

- Delete spam content

2. **Employers:**

- Post new jobs

- Manage their job listings

- View applications (future feature)

3. **Job Seekers:**

- Browse and search jobs

- Apply to jobs (future feature)

- Save job searches (future feature)

## Technology Stack

- **Backend:** Django 4.2

- **Database:** SQLite (development)

- **Frontend:** HTML/CSS, Bootstrap (optional)

- **Authentication:** Custom user model

## Project Structure

```

jobboard/

├── jobboard/          # Project config

├── jobs/              # Main app

│   ├── migrations/    # Database migrations

│   ├── templates/     # HTML templates

│   │   └── jobs/      # App-specific templates

│   ├── admin.py       # Admin config

│   ├── apps.py        # App config

│   ├── forms.py       # Form definitions

│   ├── models.py      # Database models

│   ├── tests.py       # Tests

│   ├── urls.py        # App URLs

│   └── views.py       # View functions

├── .gitignore         # Ignored files

├── manage.py          # Django CLI

├── requirements.txt   # Dependencies

└── README.md          # This file

```