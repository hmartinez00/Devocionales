import json
import os
from ManageDB.sqlite_on_db import *
from MessagesKit.msgo import tg_msgo
from General_Utilities.fecha import FechaID
from General_Utilities.option_list import option_list
from datetime import datetime as dt
from MessagesKit.str_msg_format import strmsgformat as strf
from MessagesKit.str_msg_format import buildmessage as bm

# Fecha = FechaID(dt.now())
Fecha = input('Introduzca la fecha: ')

# Definimos los source files
ruta_archivo_json = 'settings/sender/settings.json'
database = r"2tim4_1.db"
tables = os.listdir('settings/tables')
table = option_list(tables)
table = table.split('.json')[0]

# Extraemos los datos de validacion requeridos del json
with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

url = datos_json['telegram']['TELEGRAM_URL']
chat_id = datos_json['telegram']['TELEGRAM_CHAT_ID']
token = datos_json['telegram']['TELEGRAM_TOKEN']


bm(
    database,
    table,
    Fecha,
    url,
    chat_id,
    token,
).sender()