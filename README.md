\# Django Jumbo Blog Platform



A Django blog/social platform with user authentication, profiles, CRUD posts, pagination, user-specific post filtering, comments, and basic nested replies.



\## Features



\- User registration, login, and logout

\- User profiles with profile images

\- Create, read, update, and delete posts

\- Author-only post update/delete permissions

\- Paginated post feed

\- Filter posts by author

\- Comment system

\- Basic nested replies

\- Admin panel management



\## Tech Stack



\- Python

\- Django

\- SQLite

\- Bootstrap

\- Pillow

\- Django Crispy Forms



\## Current Status



Core Django backend features are working.  

Next phase: Django REST Framework APIs.



\## Setup



```bash

git clone <your-repo-url>

cd django\_project

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

