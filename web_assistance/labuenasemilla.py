from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from General_Utilities.fecha import BatchID
from General_Utilities.control_rutas import setting_routes
from modules.insertar_module import x_transport, last_date, sel_tab


key = 'blackboard'
file = setting_routes(key)[0]

# -------------------------------------
# Extraemos la fecha
# -------------------------------------
database = r"2tim4_1.db"
keys_type = True
ind = 2

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

verset_texte        = bs.find_all(class_='verset-texte'     )
verset_reference    = bs.find_all(class_='verset-reference' )
titre               = bs.find_all(class_='titre'            )
texte               = bs.find_all(class_='texte'            )
lecture             = bs.find_all(class_='lecture'          )

# -------------------------------------
# Extraemos el Titulo
# -------------------------------------
string = ''
for i in range(len(titre)):
    Titulo = str(titre[i]).split('>')[1].split('<')[0]
    string = string + Titulo + '\n'
# -------------------------------------

# -------------------------------------
# Extraemos los textos principales
# -------------------------------------
for i in range(len(verset_texte)):
    versiculo = str(verset_texte[i]).split('>')[1].split('<')[0]
    ref = str(verset_reference[i]).split('>')[1].split('<')[0]

    texto_principal = f'{versiculo} ({ref})'
    string = string + texto_principal + '\n'
# -------------------------------------

string = string + \
    'Elabore una sintesis de este devocional.'

with open(file, 'w', encoding='utf-8') as f:
    f.write(string)
f.close()

# -------------------------------------
# Enviamos a la Base de Datos
# -------------------------------------
x_transport(
        keys_type,
        database, 
        ruta_archivo_json, 
        Fecha
    )
# -------------------------------------