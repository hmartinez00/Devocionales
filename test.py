from General_Utilities.control_rutas import setting_routes


key = 'exec'
prefix = ''
sufix = ''
ruta_archivo_json = setting_routes(
    key,
    prefix,
    sufix,
)

print(ruta_archivo_json)