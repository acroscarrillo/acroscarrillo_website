# Welcome!
Code for my website www.acroscarrillo.com where I host my portfolio and some of my web projects.

# How to add a new wep project
To add a new web project like the alexpedia_40k one, create a new folder inside `web_apps/` say `web_apps/project_2_app/`. Inside `web_apps/project_2_app/`, we need to add an `web_apps/project_2_app/__init__.py` to create the new package and a `web_apps/project_2_app/view.py` to create the Flask blueprint to be passed to `app.py`. 

The contents of `web_apps/project_2_app/__init__.py` should be something like
```
# project_2_app/__init__.py
from .views import bp
```
and  the contents of `web_apps/project_2_app/view.py` something like 
```
import os
from flask import Blueprint, render_template, current_app

# Paths
HERE            = os.path.dirname(__file__)
PROJECT_ROOT    = os.path.abspath(os.path.join(HERE, os.pardir))
TEMPLATE_FOLDER = os.path.join(PROJECT_ROOT, 'templates', 'projects', 'project_2')

# Create the Blueprint
bp = Blueprint(
    'project_2',              # internal name for url_for()
    __name__,
    url_prefix='/project_2',  # mounts all routes under /project_2
    template_folder=TEMPLATE_FOLDER
)

@bp.route('/')
def index():
    """Serves templates/projects/project_2/index.html"""
    return render_template('index.html')

# Example of adding another page:
@bp.route('/details')
def details():
    """Serves templates/projects/project_2/details.html"""
    return render_template('details.html')

# If you have static assets specific to project_2, you can serve them like this:
@bp.route('/static/<path:filename>')
def project_static(filename):
    static_dir = os.path.join(PROJECT_ROOT, 'static', 'project_2')
    return current_app.send_static_file(os.path.join('project_2', filename))
```
The pages of the project_2 should be hosted in a folder inside `templates/`, i.e. `templates/project_2/`.

That's it!