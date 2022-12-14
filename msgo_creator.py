from ManageDB.sqlite_on_db import *
import json
from MessagesKit.msgo import tg_msgo
from General_Utilities.fecha import FechaID
from datetime import datetime as dt


ahora = FechaID(dt.now())

# Definimos los source files
ruta_archivo_json = 'settings.json'
database = r"2tim4_1.db"
table = 'aguas_vivas'

# Extraemos los datos de validacion requeridos del json
with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

url = datos_json['telegram']['TELEGRAM_URL']
chat_id = datos_json['telegram']['TELEGRAM_CHAT_ID']
token = datos_json['telegram']['TELEGRAM_TOKEN']


# Extraemos los datos de la base de datos

df = selectall(database, table)
df = df[df['Fecha'] == ahora].reset_index()

for i in range(len(df)):
    Versiculo = df['Versiculo'][i]
    Subtitulo = df['Subtitulo'][i]
    Pasaje = df['Pasaje'][i]
    Comentario = df['Comentario'][i]

    # Construimos los mensajes
    send_pasaje = f"*{Versiculo}*\n" + f"*{Subtitulo}*\n" + f"\n{Pasaje}"

    send_comentario = f"*{Versiculo}*\n" + f"*{Subtitulo} _(Comentario:)_*\n" + f"\n{Comentario}"


    # Enviamos los mensajes
    bot = tg_msgo(
        url,
        chat_id,
        token,
        send_pasaje,
    )

    bot.telegram_sender()