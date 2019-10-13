# -*- coding: UTF-8 -*-

import pandas as pd

from flask import Blueprint, request, render_template, redirect, url_for, session
from .modelos import Proyecto, Contacto
from .formularios import ProyectoForm, ContactoForm
from .comunes import abrir_fichero

# Definir el blueprint: establecer el prefijo url para 'gobiernodatos'
mod_gob = Blueprint('gob', __name__, template_folder='/gobernanza',
                    url_prefix='/gobiernodatos')

      
# Listado de los proyectos existentes
def listar_proyectos():
    lista_proyectos = __mostrar_proyectos()
     
    #tabla_proyectos = lista_proyectos.T
    #return render_template("proyectos.html", datos=tabla_proyectos.to_html())
    #return render_template("proyectos.html", datos=lista_proyectos.to_html())
    #return lista_proyectos.T
    return lista_proyectos.T
    
# Visualización y entrada de datos de proyecto
# def datosproyecto():
#     form = ProyectoForm(request.form)
#     
#     if form.validate_on_submit():
#         # proyecto = 
# #         proyecto = Proyecto.query.filter_by(nombreproyecto=form.nombre.data).first()
# #         
# #         if proyecto:
# #             session['id_proyecto'] = proyecto.id
# #             flash('Datos del proyecto %s' % proyecto.nombre)
# #             return redirect(url_for('proyecto.html'))
# #         
# #         flash('Introducir datos del proyecto', 'error_message')
#         pass
#     else:
#         form = request.form
#         return render_template('proyecto.html', form=form)
  
                           
# Devuelve un dataframe con los datos de los proyectos
def __mostrar_proyectos():
    proyectos = abrir_fichero("proyectos.json", "json")
    proyectos_df = pd.DataFrame.from_dict(proyectos)
    return proyectos_df  
    
# Devuelve un dataframe con los contactos de un proyecto
def __mostrar_contactos(proyecto, proyectos_df):
    contactos_df = pd.DataFrame.from_dict(proyectos_df[proyecto]["contactos"])
    return contactos_df
