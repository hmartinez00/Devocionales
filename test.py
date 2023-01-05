from bs4 import BeautifulSoup
import requests
from General_Utilities.prettify import prettify

url = 'https://www.biblegateway.com/passage/?search=G%C3%A9nesis%206&version=RVR1960'

response = requests.get(url)
bs = BeautifulSoup(response.text, 'html.parser')
links = bs.find_all('p')
# for i in links:
#     print(f'{i}\n\n')

print(prettify(links[0]))