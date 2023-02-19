from bs4 import BeautifulSoup
import requests
import webbrowser
from General_Utilities.control_rutas import setting_routes


def versiculos(__cadena__, __sub_cadena__):
    '''
    Arroja una lista de los valores de las etiquetas con atributos coincidentes con la subcadena.
    '''
    __vers__ = []
    __ref__ = []
    while True:
        ocr = str(__cadena__).find(__sub_cadena__)
        if ocr != -1:
            __cadena__ = str(__cadena__)[ocr + len(__sub_cadena__):]
            __ref__.append(__cadena__.split('"')[0])
            __num__ = __cadena__.split('-')[2].split('"')[0]
            __res__ = str(__cadena__).split('>')[3].split('<')[0]
            __string__ = f'{__num__} {__res__}'
            __vers__.append(__string__)
        elif ocr == -1:
            break
    
    return __vers__, __ref__


key         = 'blackboard'
file        = setting_routes(key)[0]

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
# Vaciar Blackboard
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
titulos = [i for i in bs.find_all('h3') if 'text' in str(i)]
titulo = ''
parrafos    = bs.find_all('p')

textos = []
string = ''
for i in range(len(parrafos)):
    if 'text' in str(parrafos[i]):
        textos.append(parrafos[i])
        
        cadena = textos[i]
        sub_cadena = 'class="text '
        # Extraemos bloque de versiculos
        vers = versiculos(cadena, sub_cadena)[0]
        # Extraemos bloque de referencias
        refs = versiculos(cadena, sub_cadena)[1]

    # -------------------------------------
    # Extraemos titulos
    # -------------------------------------
    for k in refs:
        for h in titulos:
            # Cada k del bloque de versiculos se busca en cada h_titulo
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


print(Gran_Titulo)

string = Gran_Titulo.split('Bible Gateway passage: ')[1] + '\n\n' + string

# -------------------------------------
# Actualizar Blackboard
# -------------------------------------
with open(file, 'w', encoding='utf-8') as f:
    f.write(string)
f.close()