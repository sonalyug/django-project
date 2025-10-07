# Django Blog Project

A simple and elegant blog application built with Django. This project allows users to create, view, edit, and delete blog posts, with a built-in view counter to track how many times each post is read.

## Features

- ✅ View all blog posts
- ✅ Add new blog posts
- ✅ Edit existing posts
- ✅ Delete posts with confirmation
- ✅ View counter (increases every time a post is opened)
- ✅ Clean and responsive design
- ✅ Full CRUD functionality

## Tech Stack

- Python
- Django
- HTML
- CSS

## How to Run the Project

### 1. Clone or Open the Project

Open your terminal and navigate to the project folder:
cd path/to/myblog1

text

### 2. Activate Virtual Environment

On Windows:
env\Scripts\activate

text

On Mac/Linux:
source env/bin/activate

text

### 3. Install Django (if not already installed)
pip install django

text

### 4. Run Migrations
python manage.py makemigrations
python manage.py migrate

text

### 5. Start the Development Server
python manage.py runserver

text

### 6. Open in Browser
Go to:
http://127.0.0.1:8000/blog/

text

## Project Structure

myblog1/
├── manage.py
├── myblog1/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── blog/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ └── templates/blog/
├── templates/
│ └── base.html
├── static/
│ └── css/style.css
└── db.sqlite3

text

## How It Works

- **Models**: The `Blog` model stores title, description, timestamps, and view count.
- **Views**: Handles logic for listing, creating, editing, and deleting posts.
- **Templates**: Uses Django template inheritance (`base.html`) for consistent layout.
- **Forms**: Uses Django’s `ModelForm` for easy form handling.
- **URLs**: Clean and readable URLs for each action.

## Customization Ideas

- Add user authentication (login/logout)
- Add search functionality
- Add categories or tags
- Deploy using Heroku or PythonAnywhere

## Created By

[Your Name]  
A Django learning project — built step by step to master web development.

---

> Tip: To access the admin panel, create a superuser:
> ```
> python manage.py createsuperuser
> ```
> Then go to `http://127.0.0.1:8000/admin/`
