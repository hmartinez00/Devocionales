from bs4 import BeautifulSoup
import requests
import webbrowser
import pandas as pd
import time
from General_Utilities.control_rutas import setting_routes
from modules.info_tools import general_estract


# -------------------------------------
# Extraemos los datos de la url
# -------------------------------------
url_list = [
    "http://www.doinggood.org/BibleQuizzesQFSpSound/General%20EpistlesQF/Santiago%201-2.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/General%20EpistlesQF/Santiago%203-5.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/General%20EpistlesQF/1%20Pedro%201-2.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/General%20EpistlesQF/1%20Pedro%203-5.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/General%20EpistlesQF/1%20Juan.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/General%20EpistlesQF/2%20&amp;%203%20Juan.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Apocalipsis%20w%20sd/Apocalipsis%201-5.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Apocalipsis%20w%20sd/Apocalipsis%206-11.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Apocalipsis%20w%20sd/Apocalipsis%2012-16.htm",
    "http://www.doinggood.org/BibleQuizzesQFSpSound/Apocalipsis%20w%20sd/Apocalipsis%2017-22.htm"
]


for url in url_list:
    # response    = requests.get(url                          )
    # bs          = BeautifulSoup(response.text, 'html.parser')

    # links = bs.find('title').get_text()

    # print(links)

    webbrowser.open_new_tab(url)
    time.sleep(1)