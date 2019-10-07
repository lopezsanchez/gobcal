from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
#from .frontend import index, example_form

# To keep things clean, we keep our Flask-Nav instance in here. We will define
# frontend-specific navbars in the respective frontend, but it is also possible
# to put share navigational items in here.

nav = Nav()
#icono = img(src='static/img/Escudo1.png')
nombre_app = "Gobierno y calidad de datos"

# Barra de navegación
nav.register_element('frontend_top', Navbar(
   # icono,
    nombre_app,
    View('Inicio', 'frontend.index'),
    View('Proyectos', 'frontend.proyectos_form'),
    Subgroup(
        'Documentos',
        Link('Flask-Bootstrap', 'http://pythonhosted.org/Flask-Bootstrap'),
        Link('Flask-AppConfig', 'https://github.com/mbr/flask-appconfig'),
        Link('Flask-Debug', 'https://github.com/mbr/flask-debug'),
        Separator(),
        Text('Bootstrap'),
        Link('Getting started', 'http://getbootstrap.com/getting-started/'),
        Link('CSS', 'http://getbootstrap.com/css/'),
        Link('Components', 'http://getbootstrap.com/components/'),
        Link('Javascript', 'http://getbootstrap.com/javascript/'),
        Link('Customize', 'http://getbootstrap.com/customize/'), ),
    Text('Using Flask-Bootstrap {}'.format(FLASK_BOOTSTRAP_VERSION)), ))