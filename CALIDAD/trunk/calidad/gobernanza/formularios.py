# https://plataforma.josedomingo.org/pledin/cursos/flask/curso/u19/
# https://hackersandslackers.com/guide-to-building-forms-in-flask/


from flask_wtf import FlaskForm, Form

from wtforms import StringField, FieldList, TextField, FormField, BooleanField, DateTimeField, SelectField
from wtforms.validators import InputRequired, Length, Email

class ContactoForm(FlaskForm):
    nombre = StringField("Nombre:", validators=[InputRequired()])
    email = TextField("Correo electr&oacute;nico:", validators=[Email()])
    telefono = StringField("Fijo:", validators=[Length(max=9)])
    movil = StringField("M&oacute;vil:", validators=[Length(max=9)])
    submit = SubmitField("Guardar")

class ProyectoForm(FlaskForm):
    nombre = StringField("Nombre del proyecto:", validators=[InputRequired(), Length(max=30)])
    organismo = StringField("Organismo peticionario:", validators=[InputRequired(), Length(max=50)])
    contactos = FieldList(FormField(ContactoForm), min_entries=0, max_entries=None)
    fuentes = StringField("Fichero de or&iacute;genes de datos:")
    diccionariodatos = StringField("Diccionario de datos:")
    descripcion = StringField("Descripci&oacute;n:", validators=[InputRequired()])
    submit = SubmitField("Guardar")
    
class OrigenForm(FlaskForm):
    alias = StringField("Alias:", validators=[InputRequired()])
    url = StringField("Url o ruta del fichero:", validators=[InputRequired()])
    descripcion = TextField("Descripci&oacute;n:")
    notas = TextField("Notas:")
    frecuencia = Field("Frecuencia de actualizaci&oacute;n, en minutos:", 
                       validators=[InputRequired(), NumberRange(0, 5256000)])
    ultima = DateTimeField("&Uacute;ltima actualizaci&oacute;n:")
    validado = BooleanField("Validado:", validators=[InputRequired()])
    diccionariodatos = StringField("Diccionario de datos:")
    submit = SubmitField("Guardar")
        
class CampoDatosForm(FlaskForm):
    campo = StringField("Nombre del campo:", validators=[InputRequired()])
    descripcion = StringField("Descripci&oacute;n del campo:")
    dtype = SelectField("Tipo de datos:", choices=[('String', String), 
                                                   ('Entero', Integer), ('Continuo', Float),
                                                   ('Booleano', Boolean)])
    iniciorango = StringField("Valor m&iacute;nimo del rango:")
    finrango = StringField("Valor m&aacute;ximo del rango:")
    notas = TextField("Notas:")
    submit = SubmitField("Guardar")