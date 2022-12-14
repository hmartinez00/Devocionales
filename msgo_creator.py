from ManageDB.sqlite_on_db import *
import json
from MessagesKit.msgo import tg_msgo
from General_Utilities.fecha import FechaID
from datetime import datetime as dt


# ahora = FechaID(dt.now())
ahora = input('Introduzca la fecha: ')

# Definimos los source files
ruta_archivo_json = 'settings.json'
database = r"2tim4_1.db"
table1 = 'aguas_vivas_pasajes'
table2 = 'aguas_vivas_comentarios'

# Extraemos los datos de validacion requeridos del json
with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

url = datos_json['telegram']['TELEGRAM_URL']
chat_id = datos_json['telegram']['TELEGRAM_CHAT_ID']
token = datos_json['telegram']['TELEGRAM_TOKEN']


# Extraemos los datos de la base de datos
df = selectall(database, table1)
df = df[df['Fecha'] == ahora].reset_index()

for i in range(len(df)):
    Versiculo = df['Versiculo'][i]
    Subtitulo = df['Subtitulo'][i]
    Pasaje = df['Pasaje'][i]

    # Construimos los mensajes
    send_pasaje = f"*{Versiculo}*\n" + f"*{Subtitulo}*\n" + f"\n{Pasaje}"

    # Enviamos los mensajes
    bot = tg_msgo(
        url,
        chat_id,
        token,
        send_pasaje,
    )

    bot.telegram_sender()




# Extraemos los datos de la base de datos
df = selectall(database, table2)
df = df[df['Fecha'] == ahora].reset_index()

for i in range(len(df)):
    Versiculo = df['Versiculo'][i]
    Subtitulo = df['Subtitulo'][i]
    Comentario = df['Comentario'][i]

    send_comentario = f"*{Versiculo}*\n" + f"*{Subtitulo} _(Comentario:)_*\n" + f"\n{Comentario}"

    # Enviamos los mensajes
    bot = tg_msgo(
        url,
        chat_id,
        token,
        send_comentario,
    )

    bot.telegram_sender()