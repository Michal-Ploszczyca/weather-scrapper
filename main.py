from bs4 import BeautifulSoup
from requests import get

URL = 'https://pogoda.interia.pl/'

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

def parse_city(city):
    return str(city.replace(',', ''))

for weather in bs.find_all('section', class_ = 'weather-places-group cities-weather is-legend'): #pobieramy html tabeli
    city = weather.find('ul', class_ = 'weather-index').get_text().split()

    #print(*city, sep = '\n')

    break

for x in range(0,len(city),2):
   print(city[x], city[x+1])
   if x == 30:
       break






