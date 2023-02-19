from bs4 import BeautifulSoup
import requests
import webbrowser
from General_Utilities.control_rutas import setting_routes


def ocurrencias(__cadena__, __sub_cadena__):
    '''
    Arroja una lista de los valores de las etiquetas con atributos coincidentes con la subcadena.
    '''
    __vers__ = []
    while True:
        ocr = str(__cadena__).find(__sub_cadena__)
        if ocr != -1:
            __cadena__ = str(__cadena__)[ocr + len(__sub_cadena__):]
            __vers__.append(__cadena__.split('"')[0])
        elif ocr == -1:
            break
    
    return __vers__


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
# Extraemos los datos de la pag de biblegateway
# -------------------------------------

bible = f'https://www.biblegateway.com/passage/?search={libro}+' + \
    f'{capvers}&version=RVR1960'

# webbrowser.open_new_tab(bible)

response    = requests.get(bible                        )
bs          = BeautifulSoup(response.text, 'html.parser')

parrafos    = bs.find_all('p')

textos = []
for i in range(len(parrafos)):
    if 'text' in str(parrafos[i]):
        textos.append(parrafos[i])
        
        cadena = textos[i]
        sub_cadena = 'class="text '
        vers = ocurrencias(cadena, sub_cadena)

    print(vers, cadena)

# titulos = [i for i in bs.find_all('h3') if 'text' in str(i)]

        
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