# -*- coding: UTF-8 -*-

import os

# Activamos el modo debug
DEBUG = True

# Definimos el directorio de aplicación
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Definimos la BD, en este caso, sqlite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'calidad.db')
# SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'
# SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@localhost/myapp'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Establecemos 2 threads por página
THREADS_PER_PAGE = 2

# Activamos la protección contra CSRF
CSRF_ENABLED = True

# Usamos una clave  única para firmar los datos
SECRET = os.urandom(24).hex()
CSRF_KEY = SECRET

# Usamos otra clave para las cookies
COOKIES_KEY = os.urandom(16).hex()
SECRET_KEY = COOKIES_KEY

# ------------------------------
# APP Builder
# ------------------------------
# Nombre app
APP_NAME = "Calidad de datos"

# Icono app
# APP_ICON = "static/img/logo.jpg"

# Acceso sin autenticar
AUTH_ROLE_PUBLIC = 'Public'

# ---------------------------------------------------
# Babel config for translations
# ---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = "es"
# Your application default translation path
BABEL_DEFAULT_FOLDER = "translations"
# The allowed translation for you app
LANGUAGES = {
    "es": {"flag": "es", "name": "Spanish"},
}
# ---------------------------------------------------
# Image and file configuration
# ---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = BASE_DIR + "/calidad/static/subidas/"

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = BASE_DIR + "/calidad/static/subidas/"

# The image upload url, when using models with images
IMG_UPLOAD_URL = "/static/subidas/"
# Setup image size default is (300, 200, True)
# IMG_SIZE = (300, 200, True)

# Theme configuration
# these are located on static/appbuilder/css/themes
# you can create your own and easily use them placing them on the same dir structure to override
# APP_THEME = "bootstrap-theme.css"  # default bootstrap
# APP_THEME = "cerulean.css"
# APP_THEME = "amelia.css"
# APP_THEME = "cosmo.css"
# APP_THEME = "cyborg.css"
# APP_THEME = "flatly.css"
# APP_THEME = "journal.css"
# APP_THEME = "readable.css"
# APP_THEME = "simplex.css"
# APP_THEME = "slate.css"
# APP_THEME = "spacelab.css"
# APP_THEME = "united.css"
APP_THEME = "yeti.css"
