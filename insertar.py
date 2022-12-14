from ManageDB.sqlite_on_db import *
from General_Utilities.fecha import FechaID
from datetime import datetime as dt

database = r"2tim4_1.db"
table = 'aguas_vivas_comentarios'

Fecha = FechaID(dt.now())

Versiculo = input('Introduzca los Versiculos: ')
Subtitulo = input('Introduzca el Subtitulo: ')
Texto = input('Introduzca los Texto: ')

renglon = (
    Fecha,
    Versiculo,
    Subtitulo,
    Texto
)

insert(database, table, renglon)