import json

ruta_archivo_json = 'voice_comand_settings.json'

with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

secuence_options = datos_json['voice_optiones']['secuence']

print(secuence_options[0][0])