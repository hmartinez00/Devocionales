from bs4 import BeautifulSoup
import requests
import webbrowser
from General_Utilities.control_rutas import setting_routes
from modules.info_tools import str_estract


key     = 'biblequotes'
file    = setting_routes(key)[0]
file1   = setting_routes(key)[1]

pasaje  = input('Introduzca el pasaje: ')
libro   = pasaje.split(' ')[0].lower()
string   = pasaje.split(' ')[1]
capvers = ''
for i in string:
    if i.isdigit() == False:
        char = i.encode('utf-8').hex().upper()
        capvers = capvers + f'%{char}'
    elif i.isdigit() == True:
        char = i
        capvers = capvers + f'{char}'

print(libro, capvers)

# -------------------------------------
# Vaciar passages
# -------------------------------------
string = ''
with open(file, 'w', encoding='utf-8') as f:
    f.write(string)
f.close()

# -------------------------------------
# Vaciar crossref
# -------------------------------------
string = ''
with open(file1, 'w', encoding='utf-8') as f:
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
titulos = [i for i in bs.find_all('h3') if 'text' in str(i)]
titulo = ''
parrafos    = bs.find_all('p')

list_cross_refs = [i for i in bs.find_all('li') if 'crossref-link' in str(i)]

textos = []
string = ''
for i in range(len(parrafos)):
    if 'text' in str(parrafos[i]):
        textos.append(parrafos[i])
        
        cadena = textos[i]
        sub_start = 'class="text '
        sub_end = '"'
        # Extraemos bloque de str_estract
        vers = str_estract(cadena, sub_start, sub_end)[0]
        # Extraemos bloque de referencias
        refs = str_estract(cadena, sub_start, sub_end)[1]

    # -------------------------------------
    # Extraemos titulos
    # -------------------------------------
    for k in refs:
        for h in titulos:
            # Cada k del bloque de str_estract se busca en cada h_titulo
            etiqueta = str(h).split('class="text ')[1].split('"')[0]
            titulo_0 = str(h).split('>')[2].split('<')[0]
            if k == etiqueta:
                # Si se encuentra un versiculo con titulo de entre los titulos
                # de la pagina, se asigna el titulo.
                titulo = titulo_0 # Este deberia ser el titulo del bloque vers.

    # -------------------------------------
    # Contruir parrafos
    # -------------------------------------
    sub_string = ''
    for j in vers:
        if sub_string == '':
            sub_string = sub_string + j
        elif sub_string != '':
            sub_string = sub_string + ' ' + j

    # -------------------------------------
    # Contruir el mensaje
    # -------------------------------------
    if titulo in string:
        if sub_string not in string:
            string = string + f'{sub_string}\n'
    elif titulo not in string:
            string = string + '\n' + titulo + '\n\n' + f'{sub_string}\n'

# -------------------------------------
# Extraemos referencias Cruzadas
# -------------------------------------
format_list_cross_ref = ''
for i in list_cross_refs:
    flcr = str_estract(i, 'title="Go to ', '"')
    format_list_cross_ref = format_list_cross_ref + '\n' + flcr[1][0] + ' - ' + str(flcr[0][0]).split('bibleref= ')[1]

print(format_list_cross_ref)
print(Gran_Titulo)

string = Gran_Titulo.split('Bible Gateway passage: ')[1] + '\n\n' + string

# -------------------------------------
# Actualizar passages
# -------------------------------------
with open(file, 'w', encoding='utf-8') as f:
    f.write(string)
f.close()

crossref_string = 'Referencias Cruzadas: \n' + format_list_cross_ref

# -------------------------------------
# Actualizar crossref
# -------------------------------------
with open(file1, 'w', encoding='utf-8') as f:
    f.write(crossref_string)
f.close()