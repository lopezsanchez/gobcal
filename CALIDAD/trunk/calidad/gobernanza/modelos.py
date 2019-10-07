# -*- coding: UTF-8 -*-

import pandas as pd
from .comunes import abrir_fichero, guardar_fichero

      
"""
Define el modelo de Proyecto
"""
class Proyecto():
     
    # Path del fichero json de proyectos
    __fichero_proyectos = "/proyectos/proyectos.json"
    # Todo proyecto tiene al menos un nombre que le identifique
    __proyecto_key = ""
    # Separamos el resto de parámetros para facilitar la modificacion del modelo
    __proyecto_param = {}.fromkeys(["organismo", "contactos", "ficherofuentes", "diccionariodatos", "observaciones"], "")
              
    # Función de instanciación
    def __init__(self, nombre_proyecto):
        self ={__proyecto_key : __proyecto_param}
#        self.update(__proyecto_param)
        # Contactos es un array para poder incluir varios contactos
        self[__proyecto_key]["contactos"] = []
        
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
        

    def guardar_proyecto(self, __fichero_proyectos):
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

    # Todo contacto tiene al menos un nombre
    __contacto = {"nombre":""}
    # Separamos el resto de parámetros para facilitar la modificacion del modelo
    __contacto_param = {}.fromkeys(["email", "telefono", "movil"], "")
        
    # Función de instanciación    
    def __init__(self, nombre_contacto):
        self.__contacto["nombre"] = "nombre_contacto" 
        self.__contacto.update(contacto_param)
    
    # Establecemos el resto de parametros del contacto
    def setParams(self, dic_parametros):
        for key in dic_parametros:
            self.__contacto[key] = dic_parametros[key].value()
    
    # Encapsulamos para facilitar mantenimiento          
    def getContactoParam(self, key):
        return self.__contacto[key].value()
        
    def __repr__(self):
        return '<Contacto %r>' % (self.nombre)
