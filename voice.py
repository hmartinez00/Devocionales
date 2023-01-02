from General_Utilities.control_rutas import setting_routes
from Eliezer.voice import recognizer


key = 'voice'
ruta_archivo_json = setting_routes(key)[0]
# print(ruta_archivo_json)
recognizer(ruta_archivo_json)