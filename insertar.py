from ManageDB.sqlite_on_db import *
from General_Utilities.fecha import FechaID
from datetime import datetime as dt

database = r"2tim4_1.db"
table = 'aguas_vivas_comentarios'

fecha = FechaID(dt.now())

Versiculo = input('Introduzca los Versiculos: ')
Subtitulo = input('Introduzca el Subtitulo: ')
# Pasaje = input('Introduzca el Pasaje: ')
Comentario = input('Introduzca los Comentario: ')

renglon = (
    fecha,
    Versiculo,
    Subtitulo,
    # Pasaje
    Comentario
)

insert(database, table, renglon)