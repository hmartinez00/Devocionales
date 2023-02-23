from bs4 import BeautifulSoup
import requests
import pandas as pd
from General_Utilities.control_rutas import setting_routes
from modules.info_tools import general_estract


key     = 'biblequotes'
file    = setting_routes(key)[3]

# -------------------------------------
# Vaciar polls
# -------------------------------------
string = ''
with open(file, 'w', encoding='utf-8') as f:
    f.write(string)
f.close()

libro  = input('Introduzca el nombre del libro: ')

# -------------------------------------
# Extraemos los datos de la url
# -------------------------------------
url = 'http://www.doinggood.org/BibleCourses/Spanish/spanish.asp'
# http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Numeros%201-11.htm
# http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Numeros%2012-21.htm
# http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Numeros%2022-36.htm

response    = requests.get(url                          )
bs          = BeautifulSoup(response.text, 'html.parser')

options = bs.find_all('option')

url_polls = []
for i in options:
    if 'BibleQuizzesQFSpSound/Old' in str(i) and \
        f'{libro}' in str(i):
        extract_str = str(i).split('"')[1].split('"')[0].replace('../..', 'http://www.doinggood.org').replace(' ', '%20')
        url_polls.append(extract_str)


print(url_polls)

# r_quest     = requests.get(url_polls[0]                     )
# bs0         = BeautifulSoup(r_quest.text, 'html.parser'     )

# js_questions = bs0.find('script').getText

# print(js_questions)

# cadena = str(js_questions)
# sub_start = 'initShortQuestion() {'
# sub_end = '}'
# questions = general_estract(cadena, sub_start, sub_end)

# # -------------------------------------
# # Actualizar polls
# # -------------------------------------
# string = str(js_questions)
# with open(file, 'w', encoding='utf-8') as f:
#     f.write(string)
# f.close()