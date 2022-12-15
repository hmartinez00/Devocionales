import json

tabla = input('Ingrese el nombre del archivo: ')

datos_json = \
{
    "2022-12-16":
    {
        "Ver":"Lucas 5:1-11",
        "Sub":"La pesca milagrosa",
        "Tex":""
    }
}

ruta_archivo_json = f'settings/{tabla}.json'

with open(ruta_archivo_json, 'w', encoding='utf8') as archivo_json:
    json.dump(datos_json, archivo_json, indent=4)