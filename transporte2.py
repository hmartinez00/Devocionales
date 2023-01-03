import json
from General_Utilities.control_rutas import setting_routes
from General_Utilities.option_list import option_list
from General_Utilities.fecha import format_FechaID
from modules.insertar_module import importar


# --------------------------------
# Seteando datos de iniciales
# --------------------------------
database = r"2tim4_1.db"

key = 'tables'
tables = setting_routes(key)
ruta_archivo_json = option_list(tables)
Fecha = input('Introduzca la fecha: ')
Fecha = format_FechaID(Fecha)

# --------------------------------
# Leyendo el archivo
# --------------------------------
file = r'settings\blackboard\blackboard.txt'

lines = []
with open(file, encoding='utf-8') as f:
    for line in f:
        lines.append(line)
Tit = lines[0]
Sub = lines[1]
tex = [i - 1 for i in range(len(lines))]

# --------------------------------
# Contruyendo el contenido
# --------------------------------
keys_type = input('Desea generar claves automaticas? (S/N): ')

if keys_type == 's' or keys_type == 'S':
    keys_type = 0
elif keys_type == 'n' or keys_type == 'N':
    keys_type = None

if keys_type == None:
    pass
elif keys_type != None:
    pass

# --------------------------------
# Contruyendo el diccionario
# --------------------------------
sub_param = dict(zip(tex, lines))

param = {}
param["Tit"] = Tit
param["Sub"] = Sub
param["Tex"] = sub_param

# --------------------------------
# Actualizando json
# --------------------------------
with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

datos_json[Fecha] = param

with open(ruta_archivo_json, 'w', encoding='utf8') as archivo_json:
    json.dump(datos_json, archivo_json, indent=4)

# --------------------------------
# Importar a la Base de Datos
# --------------------------------
importar(database, ruta_archivo_json, Fecha)