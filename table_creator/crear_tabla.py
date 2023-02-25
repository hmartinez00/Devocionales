import json
from ManageDB.sqlite_on_db import *


database = r"2tim4_1.db"
table = input('Introduzca el nombre de la nueva tabla: ')

ruta_archivo_json = 'settings/tables/' + table + '.json'
datos_json = {}

with open(ruta_archivo_json, 'w', encoding='utf8') as archivo_json:
    json.dump(datos_json, archivo_json, indent=4)

dict = {}
dict['Id'] = 'PRIMARY'
dict['Fecha'] = 'TEXT'


drop_table(database, table)
create_table(database, table, dict)
print(selectall(database, table))