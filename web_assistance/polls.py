from ManageDB.sqlite_on_db import *
from modules.msgo_creator_module import general_msgo_sender
from modules.insertar_module import last_date, sel_tab
from General_Utilities.fecha import format_FechaID, FechaID, DeltaT
from datetime import datetime as dt


# -------------------------------------
# Extraemos la fecha
# -------------------------------------
database = r"2tim4_1.db"
keys_type = True
# ind = 2

# ruta_archivo_json = sel_tab(
#         keys_type,
#         ind,
#     )

# Fecha = last_date(
#         False,
#         database, 
#         ruta_archivo_json
#     )

# print(Fecha)


fecha = input('Introduzca fecha: ')

ahora = format_FechaID(fecha)

for i in range(6):
    print(DeltaT(ahora, -i))
    Fecha = DeltaT(ahora, -i)

    # -------------------------------------
    # Extraemos los datos de la tabla
    # -------------------------------------
    ind = 5

    ruta_archivo_json = sel_tab(
            keys_type,
            ind,
        )

    table = str(ruta_archivo_json).split('/')[-1].split('.')[0]
    print(Fecha, table)


    df = selectall(database, table).fillna('')

    print(df.loc[df['Fecha'] == Fecha])

    print(database, table, Fecha)

    List = [
        'Lectura',
        'Titulo',
        'Intro',
        'Encuesta'
    ]
    print(general_msgo_sender(database, table, Fecha, List))