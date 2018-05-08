import bottle
import os
import sys

from bottle import TEMPLATE_PATH, static_file, route, default_app, get
project_home = os.path.dirname(os.path.abspath(__file__))

# add your project directory to the sys.path
# project_home = u'/home/supygirls/dev/SuPyGirls/src'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

application = default_app()

# Create a new list with absolute paths
# TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../view/tpl')))
# make sure the default templates directory is known to Bottle
tpl_dir = os.path.join(project_home, 'view')
img_dir = os.path.join(project_home, 'view/image')
css_dir = os.path.join(project_home, 'view/css')

if tpl_dir not in TEMPLATE_PATH:
    TEMPLATE_PATH.insert(0, tpl_dir)


@route('/')
@bottle.view('index')
def index():
    return {}


# Static Routes
@get("/image/<filepath:re:.*\.(png|jpg|svg|gif|ico)>")
def img(filepath):
    return static_file(filepath, root=img_dir)


# Static Routes
@get("/site/css/<filepath:re:.*\.(js|css|jpg)>")
def ajs(filepath):
    return static_file(filepath, root=css_dir)


if __name__ == "__main__":
    bottle.run(host='localhost', port=8080)
