import json
import os
from ManageDB.sqlite_on_db import *
from MessagesKit.msgo import tg_msgo
from General_Utilities.fecha import FechaID
from General_Utilities.option_list import option_list
from datetime import datetime as dt
from MessagesKit.str_msg_format import strmsgformat as strf
from MessagesKit.str_msg_format import buildmessage as bm
from General_Utilities.control_rutas import setting_routes


# Fecha = FechaID(dt.now())
Fecha = input('Introduzca la fecha: ')

# Definimos los source files
key = 'sender'
prefix = None
sufix = '.json'
ruta_archivo_json = setting_routes(key, prefix, sufix)[0][1]
print(ruta_archivo_json)

database = r"2tim4_1.db"

# Extraemos los datos de validacion requeridos del json
with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

url = datos_json['telegram']['TELEGRAM_URL']
chat_id = datos_json['telegram']['TELEGRAM_CHAT_ID']
token = datos_json['telegram']['TELEGRAM_TOKEN']

key = 'tables'
prefix = 'settings/tables/'
sufix = '.json'
tables = setting_routes(key, prefix, sufix)
option = option_list(tables)
table = option[0]

bm(
    database,
    table,
    Fecha,
    url,
    chat_id,
    token,
).sender()