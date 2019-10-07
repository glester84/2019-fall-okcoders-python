# Class Project Kickoff

## Week 5 objective
1. Answer any questions the class has about past lessons.
1. Create an empty django proejct on PythonAnywhere.
1. Navigate the project and identify what the files do.
1. Work through creating and documenting an API.
1. Agree on database tables/models to represent code.

## Questions from past lessons?

## Make a Django project

## Default file structure
- manage.py
- site/urls.py
- site/settings.py
- site/wsgi.py
- site/__init__.py

## Adding in a view
- site/views.py
- import into urls file
- returns some JSON content

## Using a template for content
- create a template file
- reference it in the view
- apply context data

## Create a model to store data
- relationship between models and database tables
- `./manage.py makemigrations`
- `./manage.py migrate`

## CRUD API
- Create
- Read
- Update
- Delete
- can be separate endpoints or an all-in-one

## What makes a good API design for this project?
- action-centric
- workflow-centric
- model-centric
