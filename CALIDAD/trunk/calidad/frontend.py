# -*- coding: UTF-8 -*-

"""
Se define aqui el contenido de la parte de frontend a modo de blueprint
"""
import pandas as pd

from flask import Blueprint, render_template, flash, redirect, url_for, request, session
from markupsafe import escape

from .gobernanza.controladores import listar_proyectos
from .gobernanza.formularios import ProyectoForm
from .gobernanza.modelos import Proyecto

frontend = Blueprint('frontend', __name__)

# Our index-page just shows a quick explanation. Check out the template
# "templates/index.html" documentation for more details.
@frontend.route('/')
def index():
    return render_template('index.html')


# Carga la página de proyectos.
@frontend.route('/proyectos/', methods=('GET', 'POST'))
def proyectos_form():
    
    #proyectos = listar_proyectos()
    form = ProyectoForm(request.form)
 
    if form.validate_on_submit():
        proyecto = buscar_proyecto(form.proyecto)
        proyecto["nombre_proy"] = form.proyecto
        proyecto["organismo"] = form.organismo
        proyecto["descripcion"] = form.descripcion
        proyecto.guardar_proyecto()
    else:       
        return render_template('gobernanza/proyectos.html', form=form)
       # return render_template('gobernanza/proyectos.html', tables=[proyectos.to_html(classes='data')], title=proyectos.columns.values)
                