# -*- coding: UTF-8 -*-

import pandas as pd

from flask import Blueprint, request, render_template, redirect, url_for, session
from .modelos import Proyecto, Contacto
from .formularios import ProyectoForm, ContactoForm
from .comunes import abrir_fichero

# Definir el blueprint: establecer el prefijo url para 'gobiernodatos'
mod_gob = Blueprint('gob', __name__, template_folder='/gobernanza',
                    url_prefix='/gobiernodatos')




    
@mod_gob.route('/nuevoproyecto')
def nuevoproyecto():
    form = ProyectoForm(request.form)
    
    return render_template('nuevoproyecto.html')
        
# Establecer la ruta y los  métodos aceptados
@mod_gob.route('/proyectos/', methods=['GET','POST'])
def datosproyectos():
    # Si se envían credenciales desde el formulario
    form = ProyectoForm(request.form)
    
    # Verificar datos del formulario
    if form.validate_on_submit():
        
        proyecto = Proyecto.query.filter_by(nombreproyecto=form.nombre.data).first()
        
        if proyecto:
            session['id_proyecto'] = proyecto.id
            flash('Datos del proyecto %s' % proyecto.nombre)
            return redirect(url_for('proyecto.html'))
        
        flash('Introducir datos del proyecto', 'error_message')
    else:
        form = request.form   
        return render_template('proyecto.html', form=form) 

    return render_template('proyectos.html', table=)
    data.set_index(['Name'], inplace=True)
    data.index.name=None
    females = data.loc[data.Gender=='f']
    males = data.loc[data.Gender=='m']
    return render_template('view.html',tables=[females.to_html(classes='female'), males.to_html(classes='male')],)
                           
# Devuelve un dataframe con los datos de los proyectos
def __mostrar_proyectos():
    proyectos = abrir_fichero(__fichero_proyectos, "json")
    proyectos_df = pd.DataFrame.from_dict(proyectos)  
    
# Devuelve un dataframe con los contactos de un proyecto
def __mostrar_contactos(proyecto, proyectos_df):
    contactos_df = pd.DataFrame.from_dict(proyectos_df[proyecto]["contactos"])
