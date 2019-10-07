# -*- coding: UTF-8 -*-
import logging

from flask import Flask, render_template, request, g
from flask_appbuilder import AppBuilder, SQLA
from flask_bootstrap import Bootstrap
from jinja2 import TemplateNotFound
from .nav import nav
from .frontend import frontend
#from nt import abort
#from . import vistas, controladores, modelos

"""
 Configurar logs
"""
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

"""
Definir el objeto aplicación WSGI
"""
calidad = Flask(__name__)

"""
Instalar la extension Bootstrap
"""
Bootstrap(calidad)

"""
Seguimiento de la request
"""
@calidad.before_first_request
def before_first_request():
    print("Llamada a before_first_request()")
 
@calidad.before_request
def before_request():
    print("Llamada a before_request()")
 
@calidad.after_request
def after_request(response):
    print("Llamada a after_request()")
    return response

"""
Fichero de configuraciones
"""
calidad.config.from_object("config")

"""
Inicializar la navegacion
"""
nav.init_app(calidad)

""" 
Persistencia de datos
"""
db = SQLA(calidad)

# """
# Objeto appbuilder
# """
#appbuilder = AppBuilder(calidad, db.session)

# """
# Gestión de errores
# """
# @calidad.errorhandler(404)
# def not_found():
#     return render_template('404.html')

"""
Página de inicio
"""
@calidad.route('/')
def main():
    try:
        return render_template('index.html', methods=['GET', 'POST'])
    except TemplateNotFound:
        #not_found()
        return render_template('404.html')
    
"""
Importación de  módulos de aplicación utilizando sus variables de gestión de blueprints (p. ej. mod_gob)
"""
from calidad.gobernanza.controladores import mod_gob as modulo_gobernanza

"""
Registro de blueprints
"""
calidad.register_blueprint(modulo_gobernanza)
calidad.register_blueprint(frontend)

"""
Construir base de datos
"""
db.create_all()