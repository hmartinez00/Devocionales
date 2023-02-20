from bs4 import BeautifulSoup
import requests
import pandas as pd
from General_Utilities.control_rutas import setting_routes
from modules.info_tools import str_title


key     = 'biblequotes'
file    = setting_routes(key)[2]

pasaje  = input('Introduzca el pasaje: ')
libro   = pasaje.split(' ')[0].lower()
string   = pasaje.split(' ')[1]
num = []
capvers = ''
for i in string:
    if i.isdigit() == False:
        pass
    elif i.isdigit() == True:
        char = i
        num.append(i)
    
    capvers = num[0]

print(libro, capvers)

# -------------------------------------
# Vaciar Sketch__
# -------------------------------------
string = ''
with open(file, 'w', encoding='utf-8') as f:
    f.write(string)
f.close()

# -------------------------------------
# Extraemos los datos de la pag de biblegateway
# -------------------------------------
bible = f'https://www.biblegateway.com/passage/?search={libro}+' + \
    f'{capvers}&version=RVR1960'

# webbrowser.open_new_tab(bible)

response    = requests.get(bible                        )
bs          = BeautifulSoup(response.text, 'html.parser')


Gran_Titulo = bs.find('meta', {"property":"og:title"}).get('content')

titulos = []
for i in bs.find_all('h3'):
    if 'text' in str(i):
        __cadena__      = str(i)
        titulo = str_title(__cadena__)
        titulos.append(titulo)


print(Gran_Titulo)
print(pd.DataFrame(titulos, columns = ['Pasaje', 'Titulo']))

sub_string = ''
for i in titulos:
    sub_string = sub_string + f'\n{i[0]}\t\t{i[1]}'

string = f'Bosquejo: {Gran_Titulo}\n\n' + sub_string

# -------------------------------------
# Actualizar Sketch__
# -------------------------------------
with open(file, 'w', encoding='utf-8') as f:
    f.write(string)
f.close()