import json

table = input('Introduzca el nombre de la nueva tabla: ')

ruta_archivo_json = 'settings/' + table + '.json'
datos_json = {}

with open(ruta_archivo_json, 'w', encoding='utf8') as archivo_json:
    json.dump(datos_json, archivo_json, indent=4)