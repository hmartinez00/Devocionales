from ManageDB.sqlite_on_db import *
import json
from datetime import datetime as dt
from General_Utilities.fecha import FechaID


# Fecha = FechaID(dt.now())
Fecha = input('Introduzca la fecha: ')

database = r"2tim4_1.db"
table = 'aguas_vivas_pasajes'

ruta_archivo_json = 'settings/aguas_vivas_pasajes.json'

with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

Ver = datos_json[Fecha]["Ver"]
Sub = datos_json[Fecha]["Sub"]
Tex = datos_json[Fecha]["Tex"]

for i in Tex.keys():
    texto = i + ' ' + Tex[i]

    renglon = (
        Fecha,
        Ver,
        Sub,
        texto
    )

    insert(database, table, renglon)