from datetime import datetime as dt
from General_Utilities.fecha import format_FechaID, FechaID, DeltaT

fecha = input('Introduzca fecha: ')

ahora = format_FechaID(fecha)

for i in range(10):
    print(DeltaT(ahora, -i))