import os
import json
from General_Utilities.control_rutas import setting_routes
from General_Utilities.option_list import option_list


# files = os.listdir('settings')

# tabla = option_list(files)
# print(tabla)
# ruta_archivo_json = f'settings/{tabla}'

key = 'tables'
prefix = None
sufix = '.json'
tables = setting_routes(key, prefix, sufix)
option = option_list(tables)
ruta_archivo_json = option[1]

print(ruta_archivo_json)


Fecha = input('Introduzca la fecha: ')
Tit = input('Introduzca el titulo: ')
Sub = input('Introduzca el subtitulo: ')

keys_type = input('Desea generar claves automaticas? (S/N): ')

if keys_type == 's' or keys_type == 'S':
    keys_type = 0
elif keys_type == 'n' or keys_type == 'N':
    keys_type = None

sub_param = {}

pregunta = 's'
while pregunta == 's':
    if pregunta == 's':
        string = input('Introduzca el texto: ')

        if keys_type == None:

            tex = string.split(' ')[0]

            new_string = ''
            for i in string.split(' ')[1:]:
                new_string = new_string + i + ' '

            sub_param[tex] = new_string
        
        elif keys_type != None:
            keys_type = keys_type + 1
            tex = str(keys_type) + '.'
            print(tex + ' ' + string)
            sub_param[tex] = string


        pregunta = input('Desea continuar? (s/n) ')
    else:
        break


param = {}
param["Tit"] = Tit
param["Sub"] = Sub
param["Tex"] = sub_param

# print(param)


with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

datos_json[Fecha] = param

# datos_json = \
# {
#     "2022-12-17":
#     {
#         "Ver":"Lucas 5:1-11",
#         "Sub":"La pesca milagrosa",
#         "Tex":{
#             "8":"Viendo esto Simón Pedro, cayó de rodillas ante Jesús, diciendo: Apártate de mí, Señor, porque soy hombre pecador.",
#             "9":"Porque por la pesca que habían hecho, el temor se había apoderado de él, y de todos los que estaban con él,"
#         }
#     }
# }

with open(ruta_archivo_json, 'w', encoding='utf8') as archivo_json:
    json.dump(datos_json, archivo_json, indent=4)