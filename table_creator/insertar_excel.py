import pandas as pd
from ManageDB.sqlite_on_db import *
from General_Utilities.control_rutas import setting_routes
from General_Utilities.option_list import option_list
from modules.insertar_module import importar


def redef_tupla(__tupla__):
    from General_Utilities.fecha import FechaID
    N_tupla = []
    for i in range(len(__tupla__)):
        j = __tupla__[i]
        if i == 1:
            N_tupla.append(FechaID(j))
        elif i > 1:
            N_tupla.append(j)        
    
    N_tupla = tuple(N_tupla)

    return N_tupla


database = r"2tim4_1.db"

key = 'tables'
tables = setting_routes(key)
ruta_archivo_json = option_list(tables)
table = str(ruta_archivo_json).split('/')[-1].split('.')[0]

print(table)

# val = ('a', 'a', 'a', 'a', 'a', 'a', 'a')
# insert(database, table, val)
# print(get_column_names(database, table))


archivo = r'C:\Users\admin\Documents\Estudios Biblicos\Plan Biblico Familiar\lectura 52 semanas.xlsm'

df = pd.read_excel(archivo, sheet_name='Lectura diaria').fillna('')

# for i in range(len(df)):
rows = redef_tupla(tuple(df.iloc[0]))
print(rows)
insert(database, table, rows)
