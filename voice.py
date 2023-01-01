from General_Utilities.control_rutas import setting_routes
from Eliezer.voice import recognizer


key = 'voice'
prefix = 'settings/voice/'
sufix = '.json'
ruta_archivo_json = setting_routes(
    key,
    prefix,
    sufix,
)[0]


recognizer(ruta_archivo_json)