from ManageDB.sqlite_on_db import *
from General_Utilities.control_rutas import setting_routes
from General_Utilities.option_list import option_list


database = r"2tim4_1.db"

key = 'tables'
tables = setting_routes(key)
ruta_archivo_json = option_list(tables)
table = str(ruta_archivo_json).split('/')[-1].split('.')[0]

print(table)

print(selectall(database, table))