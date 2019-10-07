"""
Se define aqui el contenido de la parte de frontend a modo de blueprint
"""
from flask import Blueprint, render_template, flash, redirect, url_for
from markupsafe import escape

from .gobernanza.formularios import ProyectosForm

frontend = Blueprint('frontend', __name__)

# Our index-page just shows a quick explanation. Check out the template
# "templates/index.html" documentation for more details.
@frontend.route('/')
def index():
    return render_template('index.html')


# Carga la página de proyectos.
@frontend.route('/proyectos/', methods=('GET', 'POST'))
def proyectos_form():
    
    form = ProyectosForm()
 
    if form.validate_on_submit():
        # We don't have anything fancy in our application, so we are just
        # flashing a message when a user completes the form successfully.
        #
        # Note that the default flashed messages rendering allows HTML, so
        # we need to escape things if we input user values:
        flash('Hello, {}. You have successfully signed up'
              .format(escape(form.name.data)))
 
        # In a real application, you may wish to avoid this tedious redirect.
        return redirect(url_for('frontend.index'))
    
    
    
    return render_template('gobernanza/proyectos.html', form=form)


    
                