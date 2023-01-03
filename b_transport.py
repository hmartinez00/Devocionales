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
<<<<<<< HEAD:transporte2.py
tex = [i - 1 for i in range(len(lines))][2:]
texto = lines[2:]

print(tex)
=======
Texto_0 = lines[2:]

>>>>>>> 06274f5452c1d2faace0bf1858d0d5651a922a52:b_transport.py

# --------------------------------
# Contruyendo el contenido
# --------------------------------
keys_type = input('Desea generar claves automaticas? (S/N): ')

if keys_type == 's' or keys_type == 'S':
    tex = [i + 1 for i in range(len(Texto_0))]
    Texto = Texto_0
elif keys_type == 'n' or keys_type == 'N':
    tex = [Texto_0[i].split(' ')[0] for i in range(len(Texto_0))]
    for i in range(len(Texto_0)):
        new_string = ''
        for i in i.split(' ')[1:]:
            new_string = new_string + ' '
            

        # Texto = Texto_0[i].split(' ')[1:]

# --------------------------------
# Contruyendo el diccionario
# --------------------------------
<<<<<<< HEAD:transporte2.py
sub_param = dict(zip(tex, texto))
=======
sub_param = dict(zip(tex, Texto))
>>>>>>> 06274f5452c1d2faace0bf1858d0d5651a922a52:b_transport.py

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

# --------------------------------
# Vaciar registro de Blackboard
# --------------------------------
string = ''
with open(file, 'w', encoding='utf-8') as f:
    f.write(string)
f.close()