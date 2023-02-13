from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from General_Utilities.fecha import BatchID
from General_Utilities.control_rutas import setting_routes
from modules.insertar_module import x_transport, last_date, sel_tab


key         = 'blackboard'
file        = setting_routes(key)[0]

# -------------------------------------
# Extraemos la fecha
# -------------------------------------
database = r"2tim4_1.db"
keys_type = True
ind = 4

ruta_archivo_json = sel_tab(
        keys_type,
        ind,
    )

print(ruta_archivo_json)

Fecha = last_date(
        keys_type,
        database, 
        ruta_archivo_json
    )

print(Fecha)

str_fecha = Fecha.replace('-', '')
fecha       = datetime.strptime(str_fecha, '%Y%m%d')
delay_fecha = BatchID(
    fecha - timedelta(days=100)
)
print(delay_fecha)
# -------------------------------------

# -------------------------------------
# Extraemos los datos de la pag de la buena semilla
# -------------------------------------
labuenasemilla = f'https://labuenasemilla.net/{delay_fecha}'

response    = requests.get(labuenasemilla               )
bs          = BeautifulSoup(response.text, 'html.parser')

lecture     = bs.find_all(class_='lecture')
Proverbio   = str(lecture).split('>')[2].split('<')[0].split('Proverbios ')[1]
cap         = int(Proverbio.split(':')[0])
vers        = Proverbio.split(':')[1]

print(type(cap), type(vers))

# -------------------------------------
# Extraemos los datos de la pag de biblegateway
# -------------------------------------
inicio = int(vers.split('-')[0])
fin = int(vers.split('-')[1])
etiquetas = [f'text Prov-{cap}-{inicio + i}' for i in range(fin - inicio + 1)]

print(etiquetas)

# bible = 'https://www.biblegateway.com/passage/?search=proverbios+' + \
#     cap + '%3A' + vers + '&version=RVR1960'

# response    = requests.get(bible                        )
# bs          = BeautifulSoup(response.text, 'html.parser')

# # vers     = bs.find_all(class_='versenum')
# sub_string = ''
# for i in etiquetas:
#     text = bs.find_all(class_=i)
#     for j in text:
#         if 'versenum' in str(j):
#             num = str(j).split('>')[2].split('<')[0]
#             cadena = str(j).split('>')[3].split('<')[0]
#             if sub_string == '':
#                 sub_string = num + ' ' + cadena
#             else:
#                 sub_string = sub_string + ' ' + num + ' ' + cadena
#         else:
#             cadena = str(j).split('>')[1].split('<')[0]
#             sub_string = sub_string + ' ' + cadena

# # -------------------------------------
# # Contruir el mensaje
# # -------------------------------------
# string = f'''Proverbios {cap}:{vers}
# {sub_string}
# Elabore una interpretacion de este texto.'''

# # -------------------------------------
# # Actualizar Blackboard
# # -------------------------------------
# with open(file, 'w', encoding='utf-8') as f:
#     f.write(string)
# f.close()

# # -------------------------------------
# # Enviamos a la Base de Datos
# # -------------------------------------
# x_transport(
#         keys_type,
#         database, 
#         ruta_archivo_json, 
#         Fecha
#     )
# # -------------------------------------