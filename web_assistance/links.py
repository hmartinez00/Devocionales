from bs4 import BeautifulSoup
import requests
import webbrowser
import pandas as pd
from General_Utilities.control_rutas import setting_routes
from modules.info_tools import general_estract


# -------------------------------------
# Extraemos los datos de la url
# -------------------------------------
url_list = [
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MajorProphets/Isaias%201-22.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MajorProphets/Isaias%2023-44.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MajorProphets/Isaias%2045-66.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MajorProphets/Jeremias%201-17.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MajorProphets/Jeremias%2018-31.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MajorProphets/Jeremias%2032-52.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MajorProphets/Lamentaciones.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MajorProphets/Ezequiel%201-21.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MajorProphets/Ezequiel%2022-48.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MajorProphets/Daniel.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MinorProphets/Oseas.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MinorProphets/Joel.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MinorProphets/Amos.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MinorProphets/Abdias.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MinorProphets/Miqueas.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MinorProphets/Nahum.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MinorProphets/Habacuc.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MinorProphets/Sofonias.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MinorProphets/Hageo.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MinorProphets/Zacarias.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/MinorProphets/Malaquias.htm"
]


for url in url_list:
    # response    = requests.get(url                          )
    # bs          = BeautifulSoup(response.text, 'html.parser')

    # links = bs.find('title').get_text()

    # print(links)

    webbrowser.open_new_tab(url)