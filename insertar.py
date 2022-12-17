import json
import os
from ManageDB.sqlite_on_db import *
from datetime import datetime as dt
from General_Utilities.fecha import FechaID
from General_Utilities.option_list import option_list

# Fecha = FechaID(dt.now())
Fecha = input('Introduzca la fecha: ')

database = r"2tim4_1.db"

tables = os.listdir('settings')
table = option_list(tables)
ruta_archivo_json = f'settings/{table}'

# table = 'aguas_vivas_pasajes'
table = table.split('.json')[0]


with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

Tit = datos_json[Fecha]["Tit"]
Sub = datos_json[Fecha]["Sub"]
Tex = datos_json[Fecha]["Tex"]

for i in Tex.keys():
    texto = i + ' ' + Tex[i]

    renglon = (
        Fecha,
        Tit,
        Sub,
        texto
    )

    insert(database, table, renglon)