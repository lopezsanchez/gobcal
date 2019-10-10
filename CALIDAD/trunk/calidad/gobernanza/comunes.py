import pandas as pd
import os
import json
from pathlib import Path
import codecs

path: Path = Path("D:/datos")


# Abre un fichero y devuelve un diccionario asociado a sus datos
def abrir_fichero(fichero, tipo):
    diccionario = {}
    filename: Path = Path(fichero)
    try:
        if tipo == "json":
            with codecs.open(path/filename, 'r', 'utf-8-sig') as f:
                diccionario = json.load(f)
        elif tipo == "csv":
            pass
        else:
            pass 
    except FileNotFoundError:
        codecs.open(path/filename, 'rw',  'utf-8-sig').close()
    return diccionario

# Guarda un diccionario en un fichero
def guardar_fichero(diccionario, fichero, tipo):
    filename: Path = Path(fichero)
    if tipo == "json":
        contenido = json.dumps(diccionario)
    elif tipo == "csv":
        pass
    else:
        pass
    with open(path/filename, "wb") as f:
        f.write(contenido, encoding="utf-8").close()
        
        
# def leer_json(file, intKey=False):
#     if "*" in file:
#         data = {}
#         for p in sorted(glob(file)):
#             year = p[-9:-5]
#             if year.isdigit():
#                 year = int(year)
#                 data[year] = read_js(p)
#         return data
#     if file and os.path.isfile(file):
#         with open(file, 'r') as f:
#             js = json.load(f)
#             if intKey:
#                 js = {int(k): v for k, v in js.items()}
#             return js
#     return None