from ManageDB.sqlite_on_db import *
import json
from datetime import datetime as dt
from General_Utilities.fecha import FechaID


ahora = FechaID(dt.now())

database = r"2tim4_1.db"
table = 'aguas_vivas'

df = selectall(database, table)
df = df[df['Fecha'] == ahora].reset_index()

print(range(len(df)))