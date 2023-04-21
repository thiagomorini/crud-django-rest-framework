# CRUD with Django REST Framework

This project is a simple CRUD built with Django REST Framework to demonstrate the basic usage of the framework. The project has two applications, the "backend" (API) and the "frontend", which allow listing, creation, modification, and deletion of modules, as well as tests of the model, views, and serializers.

## Used technologies

- Python 3.11
- Django 4.2
- Django CORS 3.14.0
- Django REST Framework 3.14.0

## Installation and execution

To run the project locally, follow these steps:

1. Clone the repository to your computer:

```
git clone https://github.com/thiagomorini/crud-django-rest-framework.git
```

2. Install the project dependencies.

3. Run the database migrations:

```
python manage.py migrate
```

4. Run the server:

```
python manage.py runserver
```

5. Access the project's API in your browser through the address http://127.0.0.1:8000/api/modules/

6. Access the project in your browser through the address http://127.0.0.1:8000/modules/

7. If you need to run tests for the model, views, and serializer, simply run the command:

```
python manage.py test backend
```

## Contribution

You can contribute to the project in several ways:

1. Reporting bugs and issues on Github.
2. Making pull requests with fixes and new features.
3. Sharing the project and encouraging other developers to use it.

## Licence
This project is distributed under the MIT license.

## Contact
You can contact me anytime you have questions or suggestions for improvement.
