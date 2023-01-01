from General_Utilities.control_rutas import setting_routes
from Eliezer.voice import recognizer


key = 'voice'
prefix = None
sufix = '.json'
ruta_archivo_json = setting_routes(
    key,
    prefix,
    sufix,
)[0][1]

# print(ruta_archivo_json)
recognizer(ruta_archivo_json)