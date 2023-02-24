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
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Genesis%201-11.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Genesis%2012-27.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Genesis%2028-37.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Genesis%2038-50.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Exodo%201-15.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Exodo%2016-40.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Levitico%201-14.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Levitico%2015-27.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Numeros%201-11.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Numeros%2012-21.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Numeros%2022-36.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Deuteronomio%201-13.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Deuteronomio%2014-21.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Old%20Testament/Deuteronomio%2022-34.htm"
]


for url in url_list:
    # response    = requests.get(url                          )
    # bs          = BeautifulSoup(response.text, 'html.parser')

    # links = bs.find('title').get_text()

    # print(links)

    webbrowser.open_new_tab(url)