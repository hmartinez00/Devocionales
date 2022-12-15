from ManageDB.sqlite_on_db import *
import json
from datetime import datetime as dt
from General_Utilities.fecha import FechaID


# Fecha = FechaID(dt.now())
Fecha = "2022-12-16"

database = r"2tim4_1.db"
table = 'aguas_vivas_pasajes'



reset_count(database, table)