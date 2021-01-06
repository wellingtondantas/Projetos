
import requests
import csv
from bs4 import BeautifulSoup as bs


MAIN_URL = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/60/fortaleza-ce'
INITIAL_CITY_URL = "2/santos-sp"

r = requests.get(MAIN_URL)

# BeautifulSoup
cities_data = []
for city in cities_list:
    r = requests.get("{}{}/{}-{}".format(MAIN_URL, city[0], slugify(city[1]), city[2].lower()))
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    months = soup.select("#mega-destaque table tbody tr")[-3:]
    for month in months:
        values = month.find_all('td')
        cities_data.append({'Cidade': city[1], 'Estado': city[2], 'Mês': values[0].text, 'Temp min(°C)': values[1].text,
                            'Temp max(°C)': values[2].text, 'Precipitação (mm)': values[3].text})


# Salva os dados capturados em um arquivo
with open('data.csv', "w") as csvfile:
    fieldnames = ['Cidade', 'Estado', 'Mês', 'Temp min(°C)', 'Temp max(°C)', 'Precipitação (mm)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in cities_data:
        writer.writerow(row)
