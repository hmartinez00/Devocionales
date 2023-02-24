from bs4 import BeautifulSoup
import requests
import pandas as pd
from General_Utilities.control_rutas import setting_routes
from modules.info_tools import general_estract


# -------------------------------------
# Extraemos los datos de la url
# -------------------------------------
url = 'https://www.youtube.com/playlist?list=PLuPPHFMyRGuJAEf8OWQHklU-I5q5-SLjq'

response    = requests.get(url                          )
bs          = BeautifulSoup(response.text, 'html.parser')

links = bs.find_all('a')

print(links)