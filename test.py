from General_Utilities.control_rutas import setting_routes


key = 'exec'
prefix = None
sufix = ''
ruta_archivo_json = setting_routes(
    key,
    prefix,
    sufix,
)[0]

print(ruta_archivo_json)