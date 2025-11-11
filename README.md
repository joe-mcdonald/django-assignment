# Django Product Catalog

A simple Django project that models products, categories, and tags, along with an admin configuration and a product listing view with search functionality.

## Features
- Models for Product, Category, and Tag.
- Admin interface for managing products, categories, and tags.
- Product listing view with search.

## Setup Instructions
1. Clone the repository.
2. Run:
```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
```
3. Use the homepage to access the product listing and search functionality.
4. Access the admin interface at `/admin` to manage products, categories, and tags.
5. Admin username is `joemcdonald`, passwrod is `ilovepython`.

## Assumptions
- The project uses Django's built-in admin interface.
- Database is included
- No frontend framework was used. I used basic HTML for templates to keep it simple.


## AI Usage
- I used chatGPT to help set up the file structure and build part of the HTLM template for the product listing view.
- I used copilot to debug an issue I had with rendering the results when a tag was applied (luckily it was just a typo).
- I used chatgpt to help build the directory tree below.

## Directory Structure
```
├── productsite
│   ├── catalog
│   │   ├── __init__.py
│   │   ├── admin.py # Contains admin configurations for Product, Category, and Tag models
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── __init__.py
│   │   │   └── 0001_initial.py
│   │   ├── models.py # Contains Product, Category, and Tag model classes
│   │   ├── templates
│   │   │   └── catalog
│   │   │       └── product_list.html # HTML template for the main product listing view
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py # Contains the product listing view with search functionality
│   ├── manage.py
│   ├── productsite
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py # includes 'catalog' app in INSTALLED_APPS
│   │   ├── urls.py # defines URL routing for the project, including the catalog app
│   │   └── wsgi.py
│   └── urls.py # Root URL configuration
├── README.md
└── requirements.txt
```