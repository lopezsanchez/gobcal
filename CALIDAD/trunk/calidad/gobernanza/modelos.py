# -*- coding: UTF-8 -*-
from calidad import db
#import pandas as pd
#from .comunes import abrir_fichero, guardar_fichero
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

"""
Define un modelo base para que el resto de tablas lo hereden
"""
class Base(db.Model):
    __abstract__ = True 
    
    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

"""    
Define el modelo de Proyecto
"""
class Proyecto(Base):
    
    __tablename__ = 'proyecto'
    
    # Datos del proyecto
    nombre = db.Column(db.String(128), nullable=False, unique=True)
    organismo = db.Column(db.String(256), nullable=False)
    contactos = db.relationship('Contacto', backref='contacto', lazy='dynamic')
    ficherofuentes = db.Column(db.String(1024))
    diccionariodatos = db.Column(db.String(1024))
    descripcion = db.Column(db.String(4096), nullable=False)
  
    # Función de instanciación
    def __init__(self, nombre, organismo, descripcion):
        self.nombre = nombre
        self.organismo = organismo
        self.ficherofuentes = ficherofuentes
        self.diccionariodatos = diccionariodatos
        self.descripcion = descripcion
        
        def __init__(self, flight=None, destination=None, check_in=None, depature=None, status=None):
            self.flight = flight
            self.destination = destination
            self.check_in = check_in
            self.depature = depature
            self.status = status
            
        

        
    # Añade los datos de un contacto al proyecto            
    def add_contacto(self, Contacto):
            self["contactos"].append(Contacto)
    
    # Busca un proyecto en el fichero json. Si no lo encuentra, crea uno nuevo
    def buscar_proyecto(self, nombre_proyecto):
        proyectos = abrir_fichero(__fichero_proyectos, "json")
        if proyectos:
            # El fichero contiene ya otros proyectos
            # Buscamos el nuestro
            for proyecto in proyectos:
                if proyecto == nombre_proyecto:
                    return proyecto_dic
        else:
            # El proyecto no existe en el fichero o bien el fichero estaba vacío
            return Proyecto(nombre_proyecto)
        

    def guardar_proyecto(self):
        proyectos = abrir_fichero(__fichero_proyectos, "json")
        # Añadimos el proyecto a la lista de proyectos
        # La clave es el nombre del proyecto y el valor el propio objeto proyecto
        proyectos.update(self)
        guardar_fichero(proyectos, __fichero_proyectos, "json")
                      
    def __repr__(self):
        return '<Proyecto %r>' % (self.proyecto)  


""" 
Define el modelo de Contacto
"""
class Contacto():

    __tablename__ = 'contacto'
    
    # Datos del contacto
    nombre = db.Column(db.String(64), nullable=False)
    apellidos = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(120))
    telefono = db.Column(db.String(9))
    movil = db.Column(db.String(9))
    
    # Función de instanciación
    def __init__(self, nombre=None, apellidos=None, email, telefono, movil):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.telefono = telefono
        self.movil = movil
        proyecto_id = db.Column(db.Integer, db.ForeignKey('proyecto.id'))
        
    def __repr__(self):
        return '<Contacto %r>' % (self.nombre)
