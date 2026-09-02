# Django Game REST API

REST API for managing video games built with Django REST Framework.

## Tech Stack
- Python / Django
- Django REST Framework
- Token Authentication
- SQLite

## Features
- CRUD operations for games
- Token-based authentication
- Custom permissions
- Search and filtering
- Pagination

## How to run locally
```bash
git clone https://github.com/sergiohdz977/Django_game_rest_api.git
cd Django_game_rest_api
python -m venv venv
venv\Scripts\activate
pip install django djangorestframework
python manage.py migrate
python manage.py runserver