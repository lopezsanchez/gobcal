# -*- coding: UTF-8 -*-

from calidad import db
#import pandas as pd
#from .comunes import abrir_fichero, guardar_fichero

# many to many with sqlalchemy https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# sqlalchemy API https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/

"""
Define un modelo base para que el resto de tablas lo hereden
"""
class Base(db.Model):
    __abstract__ = True 
    
    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


"""
Tabla que relaciona Proyectos y Contactos
"""
contactos = db.Table('contactos',
                     db.Column('proyecto_id', db.Integer, db.ForeignKey('proyecto.id'), primary_key=True),
                     db.Column('contacto_id', db.Integer, db.ForeignKey('contacto.id'), primary_key=True))

"""
Tabla que relaciones orígenes de datos (Fuentes) y Proyectos
"""
fuentes = db.Table('fuentes',
                   db.Column('proyecto_id', db.Integer, db.ForeignKey('proyecto.id'), primary_key=True),
                   db.Column('origen_id', db.Integer, db.ForeignKey('origen.id'), primary_key=True))

"""    
Define el modelo de Proyecto
"""
class Proyecto(Base):
    
    # Datos del proyecto
    nombre = db.Column(db.String(128), nullable=False, unique=True)
    organismo = db.Column(db.String(256), nullable=False)
    contactos = db.relationship('Contacto', secondary=contactos, lazy='subquery', backref=db.backref('proyectos', lazy=True))
    fuentes = db.relationship('Fuente', secondary=fuentes, lazy='subquery', backref=db.backref('proyectos', lazy=True))
    diccionariodatos = db.relationship('CampoDato', backref='proyecto', lazy=True)
    descripcion = db.Column(db.Text, nullable=False)
  
#     # Añade los datos de un contacto al proyecto            
#     def add_contacto(self, Contacto):
#             self["contactos"].append(Contacto)
#     
#     # Busca un proyecto en el fichero json. Si no lo encuentra, crea uno nuevo
#     def buscar_proyecto(self, nombre_proyecto):
# 
#     def guardar_proyecto(self):
#                       
    def __repr__(self):
        return '<Proyecto %r>' % (self.nombre)  


""" 
Define el modelo de Contacto
"""
class Contacto(Base):

    # Datos del contacto
    nombre = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(120))
    telefono = db.Column(db.String(9))
    movil = db.Column(db.String(9))
    
#     # Función de instanciación
#     def __init__(self, nombre=None, apellidos=None, email, telefono, movil):
#         self.nombre = nombre
#         self.apellidos = apellidos
#         self.email = email
#         self.telefono = telefono
#         self.movil = movil
#         proyecto_id = db.Column(db.Integer, db.ForeignKey('proyecto.id'))
        
    def __repr__(self):
        return '<Contacto %r>' % (self.nombre)

"""
Define el modelo de Origen de datos
"""
class Origen(Base):

    # Propiedades del origen de datos
    alias = db.Column(db.String(100), nullable=False)
    url = db.Column(db.Text, nullable=False)
    descripcion = db.Column(db.Text)
    notas = db.Column(db.Text)
    frecuencia = db.Column(db.Integer, nullable=False)
    ultima = db.Column(db.DateTime)
    validado = db.Column(db.Boolean)
    diccionariodatos = db.relationship('CampoDato', backref='origen', lazy=True)
    
    def __repr__(self):
        return '<Origen %r' % (self.alias)
    
"""
Define el modelo CampoDato, cuyo conjunto conforma el diccionario de datos de un proyecto o un origen de datos
"""
class CampoDato(Base):
    
    # Propiedades de cada campo de datos
    campo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    dtype = db.Column(db.String(32))
    iniciorango = db.Column(db.Integer)
    finrango = db.Column(db.Integer)
    notas = db.Column(db.Text)