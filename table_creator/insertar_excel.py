import pandas as pd
from ManageDB.sqlite_on_db import *
from General_Utilities.control_rutas import setting_routes
from General_Utilities.option_list import option_list


database = r"2tim4_1.db"
archivo = r'C:\Users\admin\Documents\Estudios Biblicos\Plan Biblico Familiar\lectura 52 semanas.xlsm'


def redef_tupla(__tupla__, index):
    from General_Utilities.fecha import FechaID
    N_tupla = []

    for i in range(len(__tupla__)):
        j = __tupla__[i]
        if i == index:
            N_tupla.append(FechaID(j))
        elif i != index:
            N_tupla.append(j)        
    
    N_tupla = tuple(N_tupla)

    return N_tupla


key = 'tables'
tables = setting_routes(key)
ruta_archivo_json = option_list(tables)
table = str(ruta_archivo_json).split('/')[-1].split('.')[0]

df = pd.read_excel(archivo, sheet_name='Lectura diaria').fillna('')

for i in range(len(df)):
    tupla = tuple(df.iloc[i])[1:]
    rows = redef_tupla(tupla, 0)
    # print(rows)
    avance = (i / len(df)) * 100
    print(avance, end='\r')
    insert(database, table, rows)

print(selectall(database, table))