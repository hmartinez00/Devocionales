import json
from ManageDB.sqlite_on_db import *
from General_Utilities.fecha import format_FechaID
from General_Utilities.option_list import option_list
from General_Utilities.control_rutas import setting_routes
from MessagesKit.str_msg_format import buildmessage as bm
from modules.msgo_creator_module import msgo_sender


Fecha = input('Introduzca la fecha: ')
Fecha = format_FechaID(Fecha)

# Definimos los source files
key = 'sender'
ruta_archivo_json = setting_routes(key)[0]
print(ruta_archivo_json)


msgo_sender(ruta_archivo_json, Fecha)

# database = r"2tim4_1.db"

# # Extraemos los datos de validacion requeridos del json
# with open(ruta_archivo_json) as archivo_json:
#     datos_json = json.load(archivo_json)

# url = datos_json['telegram']['TELEGRAM_URL']
# chat_id = datos_json['telegram']['TELEGRAM_CHAT_ID']
# token = datos_json['telegram']['TELEGRAM_TOKEN']

# key = 'tables'
# tables = setting_routes(key)
# option = option_list(tables)
# table = option.split('/')[-1].split('.')[0]

# bm(
#     database,
#     table,
#     Fecha,
#     url,
#     chat_id,
#     token,
# ).sender()