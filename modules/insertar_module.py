import json
from ManageDB.sqlite_on_db import *
from General_Utilities.fecha import format_FechaID
from General_Utilities.option_list import option_list
from General_Utilities.control_rutas import setting_routes


def importar(database, ruta_archivo_json, Fecha):

    table = ruta_archivo_json.split('/')[-1].split('.')[0]

    print(ruta_archivo_json)


    with open(ruta_archivo_json) as archivo_json:
        datos_json = json.load(archivo_json)

    Tit = datos_json[Fecha]["Tit"]
    Sub = datos_json[Fecha]["Sub"]
    Tex = datos_json[Fecha]["Tex"]

    for i in Tex.keys():
        texto = f'{i}. {Tex[i]}'

        renglon = (
            Fecha,
            Tit,
            Sub,
            texto
        )

        insert(database, table, renglon)