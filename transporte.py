import json

datos_json = \
{
    "2022-12-15":
    {
        "Ver":"Lucas 4:42-44",
        "Sub":"Jesús recorre Galilea predicando",
        "Tex":
        {
            "42":"Cuando ya era de día, salió y se fue a un lugar desierto; y la gente le buscaba, y llegando a donde estaba, le detenían para que no se fuera de ellos.",
            "43":"Pero él les dijo: Es necesario que también a otras ciudades anuncie el evangelio del reino de Dios; porque para esto he sido enviado.",
            "44":"Y predicaba en las sinagogas de Galilea."
        }
    },
    "2022-12-16":
    {
        "Ver":"Lucas 5:1-11",
        "Sub":"La pesca milagrosa",
        "Tex":
        {
            "4":"Cuando terminó de hablar, dijo (Jesús) a Simón: Boga mar adentro, y echad vuestras redes para pescar. ",
            "5":"Respondiendo Simón, le dijo: Maestro, toda la noche hemos estado trabajando, y *nada hemos pescado; mas en tu palabra echaré la red.*",
            "6":"Y habiéndolo hecho, encerraron gran cantidad de peces, y su red se rompía."
        }
    }
}

ruta_archivo_json = 'settings/aguas_vivas_pasajes.json'

with open(ruta_archivo_json, 'w', encoding='utf8') as archivo_json:
    json.dump(datos_json, archivo_json, indent=4)