# Project code

## Initial Setup
- [ ] From your PythonAnywhere account, click `+ Add a new Web App`
- [ ] Select Django as the type and choose the latest version
- [ ] Navigate into the "Project" folder that gets created and ensure there is a file named `manage.py`
- [ ] Navigate further into the "App" folder and ensure there are at least these files:
1. `__init__.py` is empty and ensures the app can be discovered in python code
1. `wsgi.py` defines the location of the main settings file and executes the "Web Server Gateway Interface" configuration
1. `settings.py` has a default config for web hosting, templates, databases, and running apps
   * we need to add our app to the list of INSTALLED_APPS
   * capitalization and spelling must match exactly
1. `urls.py` lists all the urls available on the site
1. `views.py` specifies the code that should run for each url
1. `models.py` holds the classes that will be used to make database tables for persistent data
1. `admin.py` lists all the models that can be manipulated by an admin user rather than a site user

## Turn python models into database tables
- [ ] Ensure the app folder is listed in INSTALLED_APPS in your settings file.
- [ ] Ensure your model classes are located in a file named `your_project/your_app/models.py`
- [ ] Ensure your model classes are derived from django.db.models.Model.
- [ ] Open a shell (bash) and navigate to the project folder (`cd your_project`)
- [ ] Verify that manage.py is there (`ls -a`)
- [ ] Ask django to sync the code to the database (`./manage.py makemigrations your_app`)
- [ ] Verify that it worked (`./manage.py showmigrations`)
- [ ] Run the migration it created (`./manage.py migrate`)

## After you edit code, publish it so it will appear on your site
- [ ] Save your files
- [ ] From the web tab, run "Reload <myapp.pythonanywhere.com>"
- [ ] Reload your site page

## Create an admin user to interact with the admin of your site
- [ ] Register your models with the admin site
- [ ] `./manage.py createsuperuser` and follow prompts
- [ ] in a browser, go to `yourproject.pythonanywhere.com/admin`
- [ ] Log in as the user you created
- [ ] Click around to see what you can do with your classes/models
