# Django Blog Gallery

A Django-based blog and gallery application with image uploads, CRUD functionality, and a responsive Bootstrap UI.

## Features
- Create, edit, and delete blog/gallery posts
- Image upload and media handling
- Responsive frontend using Bootstrap 4
- Django forms and templates
- SQLite database for local development

## Tech Stack
- Python
- Django
- Bootstrap 4
- SQLite (development)

## Setup Instructions

```bash
git clone https://github.com/Jwalcott02/django-blog-gallery.git
cd django-blog-gallery
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

