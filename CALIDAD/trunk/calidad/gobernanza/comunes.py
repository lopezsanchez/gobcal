import pandas as pd
import os

# Abre un fichero y devuelve un diccionario asociado a sus datos
def abrir_fichero(ruta, tipo):
    diccionario = {}
    try:
        if tipo == "json":
            js = pd.read_json(ruta)
            diccionario = json.loads(js)
        elif tipo == "csv":
            pass
        else:
            pass
    except FileNotFoundError:
        open(ruta, "w").close()
    return diccionario

# Guarda un diccionario en un fichero
def guardar_fichero(diccionario, ruta, tipo):
    if tipo == "json":
        contenido = json.dumps(diccionario)
    elif tipo == "csv":
        pass
    else:
        pass
    with open(ruta, "wb") as f:
        f.write(contenido).close()
        
        
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