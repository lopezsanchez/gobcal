from flask_wtf import FlaskForm, Form

from wtforms import StringField, FieldList, TextField, FormField
from wtforms.validators import InputRequired, Length, Email

class ContactoForm(Form):
    nombrecontacto = StringField("Nombre:")
    email = TextField("Correo electr&oacute;nico:", validators=[Email()])
    telefonomovil = StringField("M&oacute;vil:", validators=[Length(max=9)])
    telefonofijo = StringField("Fijo:", validators=[Length(max=9)])

class ProyectoForm(FlaskForm):
    nombre = StringField("Nombre del proyecto:", validators=[InputRequired(), Length(max=30)])
    organismo = StringField("Organismo peticionario:", validators=[InputRequired(), Length(max=50)])
    contactos = FieldList(FormField(ContactForm), min_entries=0, max_entries=None)
    fuentes = StringField("Fichero de or&iacute;genes de datos:")
    diccionariodatos = StringField("Diccionario de datos:")
    
    