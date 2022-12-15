from ManageDB.sqlite_on_db import *
import json
from datetime import datetime as dt
from General_Utilities.fecha import FechaID
import sqlite3

# Fecha = FechaID(dt.now())
Fecha = "2022-12-16"

database = r"2tim4_1.db"
table = 'aguas_vivas_pasajes'

campo = 'Id'
a = '1'
b = '10'

sql = 'UPDATE ' + table + ' SET ' \
f'"{campo}"={b} WHERE "{campo}"={a}'
conn = sqlite3.connect(database)
# cursor = conn.cursor()
conn.execute(sql)
conn.close()

# reset_count(database, table, campo, a, b)